
# SSOのサンプルアプリ
作り中

## djangoプロジェクト作成コマンド
docker-compose build
docker-compose run sso-web django-admin.py startproject sso_mod .

## 起動
docker-compose up -d

## containerに入る
docker exec -i -t <container id> bash