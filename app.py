import os
from spoldzielnie import init_app
from loguru import logger

current_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(current_path, 'db'))

os.environ['APP_FOLDER'] = os.path.abspath(os.path.join(current_path, 'pkgs/spoldzielnie'))
os.environ['APPDB_PATH'] = db_path 
os.environ['LOG_PATH'] = current_path   

log_level = "DEBUG"
log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> <b>{message}</b>"
logger.add(f"{os.getenv('LOG_PATH')}/file.log", level=log_level, format=log_format, colorize=False, backtrace=True, diagnose=True)


app = init_app()

if __name__ == '__main__':
    print("uruchom aplikację poprzez komendę flask run")