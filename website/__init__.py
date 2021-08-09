from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
DB_TYPE = "SQLite"


def create_app():
    # init
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'friendly-solutions'
    if DB_TYPE == "SQLite":
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    else:
        # TODO: write the other DB provider URI's
        pass
    db.init_app(app)

    # views
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # database
    from .models import Address
    create_db(app)

    return app


def create_db(app):
    if DB_TYPE == "SQLite":
        if not path.exists('website/' + DB_NAME):
            db.create_all(app=app)
            print('Database created!')