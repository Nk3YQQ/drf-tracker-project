# Результаты тестирования
[![Coverage Status](coverage/coverage-badge.svg)](coverage/coverage-report.txt)
![Workflow Status](https://github.com/Nk3YQQ/drf-tracker-project/actions/workflows/main.yml/badge.svg)

# Как пользоваться проектом

## 1) Проверти связь с удалённым сервером

Для начала нужно проверить, соединён ли Вам GitHub аккаунт с удалённым сервером ключом SSH. Для того чтобы связать GitHub с сервером, можно узнать в документации GitHub: https://docs.github.com/ru/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

## 2) Скопируйте проект на Ваш компьютер
```
git clone git@github.com:Nk3YQQ/drf-tracker-project.git
```

## 3) Настройте виртуального окружения

### Для pip
```
python3 -m env venv
```

### Для poetry
```
poetry init
```

### Активация виртуальное окружение
```
source env/bin/activate
```

## 4) Установка зависимостей

### Установка зависимостей для pip
```
pip[x] install -r requirements.txt
```

### Установка зависимостей для poetry (для UNIX-систем)
```
poetry add $(cat requirements.txt)
```

## 5) Добавьте ansible настройки в проект
### Структура директории ansible
```
dfr-tracker-project/ # Проект
...
|—— ansible/
    |—— files/
    |   |—— .env  # Файл с переменными окружения
    |—— playbook.yml  # Плейбук
    |—— inventory.ini # Файл инвентаризации
...
```

### Подсказка! 
Используйте файл .env.sample для формирования переменных окружения в файле .env

### Пример для inventory.ini
```
[<your_server_group>]
<your_server> ansible_user=<your_host_user> # Пользователь удалённого сервера
```
### Пример для playbook.yml
```
- hosts: <your_server_group> # Передаётся название группы из inventory.ini
  gather_facts: no
  become: true

  tasks:
    - name: move .env file to project in virtual server
      copy:
        src: files/.env
        dest: <your/project/path/on/remote/server> # Путь до вашего проекта на удалённом сервере
```

После настройки ansible выполните следующую команду
```
make set-env-file
```

## 6) Запуск проекта


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