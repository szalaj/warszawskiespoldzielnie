import os
from spoldzielnie import init_app
from loguru import logger
import sys

#################################################
# ustaw zmienne srodowskowe w terminalu przed uruchomieniem aplikacji
# bazy danych sqlite i
# sciezek do logow i aplikacji
###########################################
envs_to_set = [
    'APPDB_PATH',
    'LOG_PATH',
    'APP_FOLDER',
    'FLASK_SECRET_KEY'
]
# Check if APPDB_PATH is set
for env in envs_to_set:
    if not os.getenv(env):
        logger.error(f"{env} environment variable is not set")
        sys.exit(1)



log_level = "DEBUG"
log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> <b>{message}</b>"
logger.add(f"{os.getenv('LOG_PATH')}/file.log", level=log_level, format=log_format, colorize=False, backtrace=True, diagnose=True)

logger.info('uruchamiam aplikację')

app = init_app()

if __name__ == '__main__':
    print("uruchom aplikację poprzez komendę flask run")