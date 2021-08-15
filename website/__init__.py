from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from os import path


db = SQLAlchemy()


def create_app(config_file='settings.py'):
    # init
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    debug_param = app.config.get('DEBUG')
    if debug_param == 'True':
        app.debug = True
    else:
        app.debug = False
    port_param = app.config.get('PORT')
    if port_param is None:
        app.port = 5000
    else:
        app.debug = port_param
    db.init_app(app)

    # views
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # swagger
    swagger_bp = get_swaggerui_blueprint(
        app.config.get('SWAGGER_URL'),
        app.config.get('API_URL'),
        config={
            'app_name': 'Address storage API'
        }
    )
    app.register_blueprint(swagger_bp, url_prefix=app.config.get('SWAGGER_URL'))

    # database
    from .models import Address
    create_db(app, db)

    return app


def create_db(app, db):
    if app.config.get('DB_TYPE') == 'SQLite':
        if not path.exists('website/' + app.config.get('DB_NAME')):
            db.create_all(app=app)
            print('Database created!')
    else:
        # for other types of DB
        Migrate(app, db)
