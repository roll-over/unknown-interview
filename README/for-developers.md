[На главную](../README.md)

# Для разработчиков

## Стек

### Фронт

- [svelte](https://svelte.dev/)
- [typescript](<(https://www.typescriptlang.org/)>)
- [pnpm](https://pnpm.io/)
- [tailwindcss](https://tailwindcss.com/)
- [vite](https://vitejs.dev/)
- [prettier](https://prettier.io/)
- [skeleton](https://www.skeleton.dev/)

### Бэк

- [python](https://www.python.org/)
- [fastAPI](https://fastapi.tiangolo.com/)
- [mongoDB](https://www.mongodb.com/)

### Общее

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

## Pre requierments

- docker
- docker-compose
- node.js 20
- pnpm
- python 3.11

## Install and Run via docker compose

clone repository:
```
git clone git@github.com:roll-over/unknown-interview && cd unknown-interview
```
rename .env.exemple -> .env:
```
cp .env.example .env
```
run docker-compose:
```
docker-compose up --build
```
or run it as the administrator:
```
sudo docker-compose up --build
```
check in browser:
```
localhost:2080
```



[Документация по фронтенду](./../frontend/README.md)

[Документация по бекенду](./../backend/README.md)

[Команда](./command.md)

[Миссия](./mission.md)
