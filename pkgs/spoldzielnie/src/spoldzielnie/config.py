import os

class Config(object):
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/spoldzielnie/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/spoldzielnie/media"
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + f"{os.getenv('APPDB_PATH')}/dat.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = "Europe/Berlin"
    MIGRATIONS_DIR = f"{os.getenv('APP_FOLDER')}/src/spoldzielnie/migrations"