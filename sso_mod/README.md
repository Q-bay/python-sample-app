
# SSOのサンプルアプリ
作り中

## 起動
docker-compose up -d

## containerに入る
docker exec -i -t <container id> bash

# 作成に使ったコマンド
## localで 
### プロジェクト作成
docker-compose build
docker-compose run sso-web django-admin.py startproject sso .

## コンテナ内部で
python manage.py startapp mod

### migrationファイルを作る
python manage.py makemigrations

### migrationファイルを元にDBに反映する
python manage.py migrate