# modules
pythonで何かの時に使えそうなモジュールを配置していくディレクトリ

## ツール説明

### converter
コマンドラインツール
キャメルケース、スネークケースの変換する
下記コマンドで実行可能
python converter.py

# Docker操作について
## コマンド：Dockerイメージのビルドから起動
docker-compose up -d --build

## 起動&デーモン化
docker-compose up -d

## コンテナに入る
docker-compose exec python3_modules bash

## 停止
docker-compose down
