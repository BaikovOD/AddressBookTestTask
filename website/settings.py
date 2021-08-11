import os
from dotenv import load_dotenv

load_dotenv()

# DB Settings
DB_NAME = os.getenv('DB_NAME')
DB_TYPE = os.getenv('DB_TYPE')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Keys
SECRET_KEY = os.getenv('SECRET_KEY')
API_KEY = os.getenv('API_KEY')


