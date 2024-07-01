import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.getenv('API_KEY')
    BASE_URL = os.getenv('BASE_URL')
    YEARS = 5
    