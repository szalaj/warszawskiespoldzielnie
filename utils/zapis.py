
# run with m switch from web/ $ python -m project.write_seed
from spoldzielnie import init_app , db

from spoldzielnie.models import Spoldzielnia
import csv
import datetime
import os
import random
import pandas as pd
import numpy as np



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
\
def load_spoldzielnie():
    with app.app_context():

        df = pd.read_csv('../pkgs/spoldzielnie/spoldzielnie/static/warszawskie_spoldzielnie.csv',dtype=str, header=0, sep=',', encoding='utf-8')
        
        print(df.head())


        #print(inflacja_mm)
        for index, row in df.iterrows():
            print('row-------')
            print(row['data_rejestracji'])
            if pd.isna(row['data_rejestracji']):
                #print('nan')
                print('aha')
                pass
            else:
                print('not nan' )
               
                if row['data_rejestracji']=='':
                    print('aaa')

            # check if data rejestracji is empty
            
            
            # data = f"{row['Rok']}-{row['Miesiac']:02d}"
            # wartosc = float(row['Wartosc'].replace(',','.'))
            d = Spoldzielnia(
                nazwa=row['nazwa'],
                krs=row['krs'],
                nip=row['nip'],
                regon=row['regon'],
                adres=row['adres'],
                kod_pocztowy=row['kod_pocztowy'],
                miejscowosc=row['miejscowosc'],
                forma_prawna=row['forma_prawna'],
                data_rejestracji=None if pd.isna(row['data_rejestracji']) else datetime.datetime.strptime(row['data_rejestracji'], '%Y-%m-%d'),
                status=row['status'],
                szerokosc_geo=row['szerokosc_geo'],
                dlugosc_geo=row['dlugosc_geo']
            )
            db.session.add(d)
            db.session.commit()

if __name__ == "__main__":
    print('ehlo')
    load_spoldzielnie()