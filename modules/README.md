# modules
pythonで何かの時に使えそうなモジュールを配置していくディレクトリ

## ツール説明

### converter.py
コマンドラインツール
キャメルケース、スネークケースの変換する
下記コマンドで実行可能
python converter.py

### dynamodb_crud.py
dynamodbに対して操作するツール
今後dynamodbの操作をする上で使いまわせるコードなどを入れる予定

### create_table.py
テスト用テーブル作成ファイル

# Docker操作について(メモ書き)
## コマンド：Dockerイメージのビルドから起動
docker-compose up -d --build

## 起動&デーモン化
docker-compose up -d

## コンテナに入る
docker-compose exec python3_modules bash

## 停止
docker-compose down

## コンテナ一覧(-aで停止コンテナも取得)
docker ps -a

下記のように取得できる
PS C:\work_space_python_toranoko\modules> docker ps -a
CONTAINER ID   IMAGE                     COMMAND                  CREATED        STATUS                     PORTS     NAMES
6f986b100678   modules_python3_modules   "python3"                6 days ago     Up About a minute                    modules_python3_modules_1

## コンテナ停止
docker stop \<container id or container name>
