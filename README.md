# Проект: Оценка недвижимости


## Описание

Проект представляет собой сайт, на котором есть возможность посмотреть базу данных квартир, добавить в эту базу свою квартиру и оценить стоимость своей квартиры, 
заполнив необходиые параметры. 
Написан на языке Python с использованием фреймворка Flask, а также библиотек Flask WTF Form для работы с формами, Flask-SQLAlchemy для работы с базой данных,
Сianparser для парсинга сайта cian.ru для создания базы квартир, Catboost для обучения модели предсказания стоимости квартиры.

## Установка и запуск

1. Склонировать репозиторий на свой компьютер

```bash
git clone git@github.com:BugZ-EKB/cian_estimate.git
```
или
```bash
git clone https://github.com/hodakoov/advertising_site.git
```

2. Перейти в папку с проектом 
```bash
cd cian_estimate
```

3. Создать и активировать виртуальное окружение (для Windows)
```bash
python3 -m venv venv
.\env\Scripts\activate
```

4.Установить необходимые зависимости

```bash
   pip install -r requirements.txt
```

5. Запустить проект (для Windows)
```bash
.\run
```

6. Откройте веб-браузер и перейдите по адресу http://127.0.0.1:5000/ или http://localhost:5000.


## Используемые технологии

- `Python 3.10`
- `Flask 3.0.0`
- `Flask WTF Form 1.2.1`
- `Flask SQLAlchemy 3.1.1`
- `Catboost 1.2.2`

### База данных
На данный момент используется `SQLite`, которая поставляется месте с Python.


## Авторы

- [Шорохов Егор](https://t.me/egor_shorohov)
- [Анучин Николай](https://t.me/ickname)

## Благодарности

- Нашему ментору [Синякову Глебу](https://t.me/technogleb) 
- Команде [LearnPython](https://learn.python.ru/)
