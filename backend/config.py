from decouple import AutoConfig
import os


config = AutoConfig()
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'database.db')

class Config:
    SECRET_KEY = config('SECRET_KEY', default='your-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default=f"sqlite:///{DATABASE_PATH}")
    DEBUG = True
    SQLALCHEMY_ECHO = True

config_dict = {
    'development': DevConfig
}