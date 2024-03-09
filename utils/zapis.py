
# run with m switch from web/ $ python -m project.write_seed
from spoldzielnie import init_app , db

from spoldzielnie.models import Spoldzielnia
import csv
import datetime
import os
import random



current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
db_path = os.path.abspath(os.path.join(current_path, 'db'))
os.environ['APP_FOLDER'] = os.path.abspath(os.path.join(current_path, 'pkgs/spoldzielnie'))

os.environ['APPDB_PATH'] = db_path 
os.environ['LOG_PATH'] = current_path   

app=init_app()

def load_bank():
    with app.app_context():
        #db.init_app(app)
        #print(inflacja_mm)
        # for i in range(13):
            
        # d = Spoldzielnia(
        #     nazwa="ROBOTNICZA SPÓŁDZIELNIA MIESZKANIOWA URSUS",
        #     krs="0000065997",
        #     nip="5250006288",
        #     regon="000492210",
        #     adres="ul. SOSNKOWSKIEGO 11",
        #     kod_pocztowy="02-495",
        #     miejscowosc="WARSZAWA",
        #     forma_prawna="Spółdzielnia",
        #     data_rejestracji=datetime.datetime.now(),
        #     status="Działa",
        #     szerokosc_geo="52.2155",
        #     dlugosc_geo="20.9053"
        # )
        d = Spoldzielnia(
            nazwa='SPÓŁDZIELNIA MIESZKANIOWA "STARÓWKA"',
            krs="0000224292",
            nip="5250012260",
            regon="000489774",
            adres="ul. Pańska 59",
            kod_pocztowy="00-830",
            miejscowosc="WARSZAWA",
            forma_prawna="Spółdzielnia",
            data_rejestracji=datetime.datetime.now(),
            status="Cyk",
            szerokosc_geo="52.2318",
            dlugosc_geo="20.9956"
        )
        print(d)
        print(db)
        db.session.add(d)
        db.session.commit()

if __name__ == "__main__":
    print('ehlo')
    load_bank()