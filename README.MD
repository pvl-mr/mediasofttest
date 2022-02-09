
## _О проекте_
Автор: Павлова Мария.  <br />
Тестовое задание Python расположено в корне проекта. <br />
Используемые технологии: django-rest-framework, postgresql.

## _Установка *_
# Предварительные требования
```sh
Python 3.8.8, pip 20.2.3, git, postgresql
```
# 0. Создать пустую бд в postgresql согласно настройкам, указаным в setings.py DATABASES, 
# 1. Клонирование проекта
```sh
git clone https://github.com/pvl-mr/mediasofttest/
cd mediasofttest/
```
# 2. Создание и активация виртуального окружения
```sh
python -m venv venv
source ./venv/Scripts/activate
```
# 3. Установка необходимых пакетов
```sh
pip install -r requirements.txt
```
# 4. Выполнить миграции бд **
```sh
python shopsite/manage.py makemigrations
python shopsite/manage.py migrate
```
# 5. Запуск сервера
```sh
python shopsite/manage.py runserver
```

*Все команды выполнены в git bash OC Windows.
** После выполнения миграций заполнить бд на своё усмторение.
