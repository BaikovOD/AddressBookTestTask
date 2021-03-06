import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')

# DB Settings
DB_NAME = os.getenv('DB_NAME')
DB_TYPE = os.getenv('DB_TYPE')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Keys
SECRET_KEY = os.getenv('SECRET_KEY')
API_KEY = os.getenv('API_KEY')

# SWAGGER
SWAGGER_URL = os.getenv('SWAGGER_URL')
API_URL = os.getenv('API_URL')



