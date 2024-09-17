# algorithm
アルゴリズムの練習用

## アルゴリズムについて
### sieve_of_eratosthenes.py
エラストテネスの篩のアルゴリズム
素数を出す分には問題ないが遅いので改良する予定

## コマンド操作について
### コマンド：Dockerイメージのビルドから起動
docker-compose up -d --build

### 起動&バックグラウンド起動
docker-compose up -d

### コンテナに入る
docker-compose exec python3_algorithm bash

### 停止
docker-compose down
