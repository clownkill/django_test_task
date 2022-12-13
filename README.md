# Тестовое задание DRF
 
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

Тестовое задание Django Rest Framework. API для работы с товарами.


### Требования

Для запуска проекта необходимо:
- Python 3.10

### Переменные окружения

Определите переменные окружения в файле `.env` в формате: `ПЕРЕМЕННАЯ=значение`:
- `DEBUG` — дебаг-режим. Поставьте `True` для включения, `False` — для 
выключения отладочного режима. По умолчанию дебаг-режим отключен.
- `SECRET_KEY` — секретный ключ проекта, например: `fwei3$@K!fjslfji;erfkdsewyiwerlfskfhfjdslfsf3`
- `ALLOWED_HOSTS` — список разрешенных хостов.

## Установка и запуск на локальном сервере

- Скачайте код из репозитория
- Установите зависимости командой:
```shell
pip install -r requirements.txt
```
- Создайте файл `.env` в корневой папке и пропишите необходимые переменные 
окружения в формате: `ПЕРЕМЕННАЯ=значение`


- Выполните миграцию БД:
```commandline
python manage.py makemigrations
python manage.py migrate
```
- Запустите скрипт командой:
```commandline
python manage.py runserver
```


### Панель администратора

Панель администратора сайта доступна по адресу `sitename/admin/`. Для
создания учетной записи администратора используйте команду:
```commandline
python manage.py createsuperuser
```
