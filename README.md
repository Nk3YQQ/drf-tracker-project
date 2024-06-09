# Результаты тестирования
[![Coverage Status](coverage/coverage-badge.svg)](coverage/coverage-report.txt)
![Workflow Status](https://github.com/Nk3YQQ/drf-tracker-project/actions/workflows/main.yml/badge.svg)

# Как пользоваться проектом

## 1) Проверти связь с удалённым сервером

Для начала нужно проверить, соединён ли Ваш GitHub аккаунт с удалённым сервером ключом SSH. Для того чтобы связать GitHub с сервером, можно узнать в документации GitHub: https://docs.github.com/ru/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

## 2) Скопируйте проект на Ваш компьютер
```
git clone git@github.com:Nk3YQQ/drf-tracker-project.git
```

## 3) Добавьте ansible настройки в проект
Для начала скачайте ansible на вашу локальную машину:
```
pip[x] install ansible
```
Далее создайте папку ansible в корне проекта и опишите её по инструкции
### Структура директории ansible:
```
dfr-tracker-project/ # Проект
...
|—— ansible/
    |—— files/
    |   |—— .env  # Файл с переменными окружения
    |   |—— Dockerfile  # Файл для образа nginx
    |—— templates
    |   |—— nginx.conf.j2  # Файл для будущей конфигурации nginx-образа
    |—— deploy.yml  # Плейбук для деплоя
    |—— inventory.ini # Файл инвентаризации
...
```

### Подсказка! 
Используйте файл .env.sample для формирования переменных окружения в файле .env

### Пример для inventory.ini:
```
[<your_server_group>]
<your_server> ansible_user=<your_host_user> # Пользователь удалённого сервера
```
### Пример для deploy.yml:
```
- hosts: <your_server_group> # Передаётся название группы из inventory.ini
  gather_facts: no
  become: true
  
  vars:
    server_name: <your_server_ip>
    packages:
      - postgresql
      - postgresql-contrib
      - python3-venv
      - nginx
      - git
    project_path: <your/project/path/on/remote/server> # Путь до вашего проекта на удалённом сервере

  tasks:
    - name: update packages and install important dependencies for server
      apt:
        name: "{{ item }}"
        update_cache: yes
      loop:
        "{{ packages }}"
      tags:
        - "install_dependencies"

    - name: create directory for project
      file:
        path: "{{ project_path }}"
        state: directory
        mode: '0700'
      tags:
        - deploy


    - name: clone project
      git:
        repo: 'git@github.com:Nk3YQQ/drf-tracker-project.git'
        dest: "{{ project_path }}"
        version: main
        update: yes
        force: yes
      tags:
        - deploy

    - name: create nginx directory in project
      file:
        path: "{{ project_path }}/nginx"
        state: directory
        mode: '0700'
      tags:
        - deploy

    - name: copy nginx.conf.j2
      template:
        src: templates/nginx.conf.j2
        dest: "{{ project_path }}/nginx"
      tags:
        - deploy

    - name: rename nginx.conf.j2 to nginx.conf
      command:
        cmd: mv "{{ project_path }}/nginx/nginx.conf.j2" "{{ project_path }}/nginx/nginx.conf"
      tags:
        - deploy

    - name: copy Dockerfile for nginx image
      copy:
        src: files/Dockerfile
        dest: "{{ project_path }}/nginx"
      tags:
        - deploy

    - name: copy .env file to project in virtual server
      copy:
        src: files/.env
        dest: "{{ project_path }}"
      tags:
        - deploy

    - name: run project
      shell:
        cmd: "make deploy-project"
      args:
        chdir: "{{ project_path }}"
      tags: "run"
```

### Пример для nginx.conf.j2:
```
server {

    listen 80;
    server_name {{ server_name }};

    location / {
        proxy_pass http://drf:8000;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /app/static/;
    }

    location /media/ {
        alias /app/media/;
    }

}
```

### Пример для Dockerfile
```
FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
```

После настройки ansible выполните следующую команду:
```
make deploy
```

## 4) Запуск проекта
После полной настройки проекта, необходимо выполнить следующую команду:
```
make run
```

# *Опционально
Если Вы хотите как-нибудь подстроить проект под себя (например поработать в виртуальном окружении), то следуйте следующим шагам:

## 1) Настройте виртуального окружения

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

## 2) Установка зависимостей

### Установка зависимостей для pip
```
pip[x] install -r requirements.txt
```

### Установка зависимостей для poetry (для UNIX-систем)
```
poetry add $(cat requirements.txt)
```

# Основные команды

### Запуск сервера (для тестирования)
```
make runserver
``` 

### Запуск тестов (для развёртывания)
``` 
make runserver-prod
```

### Запуск тестов для github actions
```
make tests
```

### Установка зависимостей для сервера
```
make install-dependencies
```

### Деплой проекта с ansible
```
make deploy
```

### Деплой проекта с docker-compose
```
make deploy-project
```

### Проверка контейнеров на сервере после запуска проекта
```
make check-containers
```

### Запуск celery и celery-beat
```
make celery-worker
make celery-beat
```

### Запуск телеграмм бота в контейнере приложения
```
make bot-run
```

### Запуск проекта
```
make run
```