# Addressbook API

Address storage with GET and ADD API endpoints. Task link: https://gist.github.com/aryou/1f0861ac855085c5887ce441d7416270

Integration with Flask-SQLalchemy.

### Extension:
- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Testing: [pytest](https://docs.pytest.org/)

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
│   .gitignore
│   main.py
│   Readme.md
│   requirements.txt
│
└───website
    │   .env
    │   address_book.db
    │   address_operations.py
    │   models.py
    │   settings.py
    │   views.py
    │   __init__.py
    │
    ├───static
    │       swagger.json
    │
    ├───templates
    │       addresses.html
    │       addresses_import.html
    │       address_add.html
    │       base.html
    │
    ├───tests
    │   │   api_test.py
```
## Flask Configuration

to configure the Flask go to /website/.env file
#### .env file

```
PORT = 5000
DEBUG = False

DB_TYPE = "SQLite"
DB_NAME = "address_book.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///address_book.db"

SECRET_KEY = "friendly-solutions"
API_KEY = "ADDRESSES-API"

SWAGGER_URL = "/api-doc"
API_URL = "/static/swagger.json"
```

 
## Run Flask
### Run flask for develop
```
$ python main.py
```
Swagger document page:  `http://127.0.0.1:port/api-doc/`


## Unittest
```
$ pytest
```


### Run with Docker

```
$ docker build -t address-book:flask

$ docker run -p 5000:5000 -it --rm --name address-book address-book:flask
 
```

In image building, the webapp folder will also add into the image