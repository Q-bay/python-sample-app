import boto3
import time
import os
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

STOP_FLAG_KEY = 'STOP_DELETION'

def should_stop():
    return os.environ.get(STOP_FLAG_KEY, 'false').lower() == 'true'

def delete_old_objects(bucket, cutoff_year, max_keys=1000, continuation_token=None, time_limit=None):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    
    def get_year(key):
        parts = key.split('/')
        for part in parts:
            if part.isdigit() and len(part) == 4:
                return int(part)
        return None

    def should_delete(key):
        year = get_year(key)
        return year is not None and year <= cutoff_year

    total_deleted = 0
    start_time = time.time()
    
    try:
        while True:
            # タイムアウトチェック
            if time_limit and time.time() - start_time > time_limit - 5:
                logger.info("タイムアウトが近いため、処理を中断します。")
                return total_deleted, continuation_token

            if should_stop():
                logger.info("停止フラグが検出されました。処理を中断します。")
                break

            pagination_args = {
                'Bucket': bucket,
                'PaginationConfig': {'MaxItems': max_keys}
            }
            if continuation_token:
                pagination_args['ContinuationToken'] = continuation_token

            page_iterator = paginator.paginate(**pagination_args)

            for page in page_iterator:
                if 'Contents' not in page:
                    continue
                
                delete_keys = [{'Key': obj['Key']} for obj in page['Contents'] if should_delete(obj['Key'])]
                
                if delete_keys:
                    response = s3.delete_objects(Bucket=bucket, Delete={'Objects': delete_keys})
                    deleted = len(response.get('Deleted', []))
                    total_deleted += deleted
                    logger.info(f"{deleted}個のオブジェクトを削除しました。合計: {total_deleted}")
                
                time.sleep(0.1)

                # 各ページ処理後にもタイムアウトチェック
                if time_limit and time.time() - start_time > time_limit - 5:
                    logger.info("タイムアウトが近いため、処理を中断します。")
                    return total_deleted, page.get('NextContinuationToken')

            if 'NextContinuationToken' not in page:
                continuation_token = None
                break
            continuation_token = page['NextContinuationToken']
    
    except ClientError as e:
        logger.error(f"S3操作失敗: {e}")
        raise

    return total_deleted, continuation_token

def lambda_handler(event, context):
    bucket = event.get('bucket')
    year = event.get('year')
    max_keys = event.get('max_keys', 1000)
    continuation_token = event.get('continuation_token')
    
    if not bucket or not year:
        return {
            'statusCode': 400,
            'body': '必須パラメータが不足しています: bucket と year'
        }
    
    try:
        cutoff_year = int(year)
    except ValueError:
        return {
            'statusCode': 400,
            'body': '無効な年フォーマットです。有効な整数を指定してください。'
        }
    
    # Lambda関数の残り実行時間を取得（ミリ秒単位）
    time_limit = context.get_remaining_time_in_millis() / 1000  # 秒単位に変換
    
    try:
        total_deleted, next_continuation_token = delete_old_objects(
            bucket, cutoff_year, max_keys, continuation_token, time_limit
        )
        
        response = {
            'statusCode': 200,
            'body': f'{bucket}内の{cutoff_year}年以前のオブジェクトを{total_deleted}個削除しました。'
        }
        
        if next_continuation_token:
            response['continuation_token'] = next_continuation_token
            response['body'] += ' 処理は完了していません。続きを実行してください。'
        else:
            response['body'] += ' 全ての処理が完了しました。'
        
        return response
    except Exception as e:
        logger.error(f"予期せぬエラー: {e}")
        return {
            'statusCode': 500,
            'body': '内部サーバーエラーが発生しました。ログを確認してください。'
        }