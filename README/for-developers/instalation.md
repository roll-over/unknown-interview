[На главную](../README.md) > [Для разработчиков](./../for-developers.md)

## Install and Run via docker compose

clone repository:

```
git clone git@github.com:roll-over/unknown-interview && cd unknown-interview
```

rename .env.exemple -> .env:

```
mv .env.example .env
```

run docker-compose:

```
docker-compose up --build
```

or run it as the administrator:

```
sudo docker-compose up --build
```

check in browser http://localhost:2080/