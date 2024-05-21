# Результаты тестирования
[![Coverage Status](coverage/coverage-badge.svg)](coverage/coverage-report.txt)
![Workflow Status](https://github.com/Nk3YQQ/drf-tracker-project/actions/workflows/main.yml/badge.svg)

# Установка зависимостей

Перед запуском убедитесь, что Вы установили виртуальное окружение и скачали зависимости.

## Установка зависимостей для pip
```
pip install -r requirements.txt
```

## Установка зависимостей для poetry (для UNIX-систем)
```
poetry add $(cat requirements.txt)
```

# Основные команды

## Запуск сервера
```
make runserver
``` 

## Запуск тестов
``` 
make tests
```

## Запуск телеграм-бота 

```
make bot-run
```

## Запуск coverage
```
make coverage
```

Обязательно ознакомитесь с файлом .env.sample, где представлены примеры заполнения переменных окружения.