# Тесты

## Запуск тестов

```bash
docker-compose -f docker-compose.test.yml up
```

## e2e tests

e2e тесты написаны на python + pytest + playwright.

### Запуск тестов

```bash
cd tests/e2e_testing
pytest
```

или

```bash
cd ..
docker-compose -f docker-compose.test.yml up e2e-test
```

### Установка зависимостей

```bash
pip install -r requirments.txt
```

## api tests

api тесты написаны на python + pytest + requests.

### Запуск тестов

```bash
cd api_testing
pytest
```

или

```bash
cd ..
docker-compose -f docker-compose.test.yml up api-test
```
