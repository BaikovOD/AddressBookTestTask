# Addressbook API

Address storage with get and add API endpoints

Integration with Flask-restplus, Flask-Cors, Flask-SQLalchemy extensions.

### Extension:
- Restful: [Flask-restplus](http://flask-restplus.readthedocs.io/en/stable/)

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

to configure the Flask go to .env file
#### cfg example (.env)

```
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
In flask, Default port is `5000`

Swagger document page:  `http://127.0.0.1:5000/api-doc`


## Unittest
```
$ pytest
```
