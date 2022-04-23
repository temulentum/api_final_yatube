## Api_yatube

Учебный проект, API для блог-платформы

### Как запустить проект:

Клонировать репозиторий создать и активировать виртуальное окружение, установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов

Запрос на получение всех постов:

```
http://127.0.0.1:8000/api/v1/posts/
```

Ответ:

```
{

    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 

[

        {}
    ]

}
```