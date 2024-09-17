# environment_for_python
dockerでのpython環境構築用

## コマンド：Dockerイメージのビルドから起動
docker-compose up -d --build

## 起動&バックグラウンド起動
docker-compose up -d

## コンテナに入る
docker-compose exec python3 bash

## 停止
docker-compose down
