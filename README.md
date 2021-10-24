# vantan-mysite

起動方法

DBの起動に時間がかかり、DBが起動しないとDjangoが起動しないため、まずDBを起動します。

```sh
docker-compose up -d django-db
```

1〜2分くらい待って、Djangoを起動します。

```sh
docker-compose up -d django
```

http://localhost:8000/ で、Djangoにアクセスできます。
