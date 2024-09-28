# s3_folder_deleter.py
S3のバケットで不要ログを削除するために作成
以下みたいにイベントで指定する

```
{
  "bucket": "対象バケット",
  "year": "2023",
  "max_keys": 10000
}
```

```

{
  "bucket": "対象バケット",
  "year": "2023",
  "max_keys": 1000,
  "continuation_token": "hogehoge"
}
```
