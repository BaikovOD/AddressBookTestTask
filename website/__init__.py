from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()


def create_app(config_file='settings.py'):
    # init
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)

    # views
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # database
    from .models import Address
    create_db(app)

    return app


def create_db(app):
    if app.config.get("DB_TYPE") == "SQLite":
        if not path.exists('website/' + app.config.get("DB_NAME")):
            db.create_all(app=app)
            print('Database created!')