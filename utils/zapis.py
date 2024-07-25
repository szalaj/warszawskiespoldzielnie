
# run with m switch from web/ $ python -m project.write_seed
from spoldzielnie import init_app , db

from spoldzielnie.models import Spoldzielnia, Sprawa, Walne
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

def load_sprawy():
    with app.app_context():

        file_path = os.path.join(current_path, 'pkgs/spoldzielnie/src/spoldzielnie/dane/sprawy.ods')

        df = pd.read_excel(file_path,dtype=str, header=0)

        #print(df.head())

        for index, row in df.iterrows():
            krs = row['spoldzielnia_krs']
            zera = 10 - len(str(krs))
            krs = '0'*zera + str(krs)
            print(krs)
            d = Sprawa(
                spoldzielnia=krs,
                zgloszenie=row['zgloszenie'],
                kontakt=row['kontakt'],
                data_rozpoczenia=None if pd.isna(row['data_rozpoczenia']) else datetime.datetime.strptime(row['data_rozpoczenia'], '%Y-%m-%d'),
                data_zakonczenia=None if pd.isna(row['data_zakonczenia']) else datetime.datetime.strptime(row['data_zakonczenia'], '%Y-%m-%d'),
                opis=row['opis'],
                status=row['status'],
                rozwiazanie=row['rozwiazanie'],
                kategoria=row['kategoria'],
                odnosniki=row['odnosniki'],
                uwagi=row['uwagi'],
                szerokosc_geo=row['szerokosc_geo'],
                dlugosc_geo=row['dlugosc_geo']
            )
            db.session.add(d)
            db.session.commit()

def load_spoldzielnie():
    with app.app_context():

        df = pd.read_excel( os.path.join(current_path, 'pkgs/spoldzielnie/src/spoldzielnie/dane/spoldzielnie.ods'),dtype=str, header=0)




        for index, row in df.iterrows():
            krs = row['krs']
            zera = 10 - len(str(krs))
            krs = '0'*zera + str(krs)          
            
            d = Spoldzielnia(
                nazwa=row['nazwa'],
                krs=krs,
                nip=row['nip'],
                regon=row['regon'],
                adres=row['adres'],
                dzielnica=row['dzielnica'],
                kod_pocztowy=row['kod_pocztowy'],
                miejscowosc=row['miejscowosc'],
                forma_prawna=row['forma_prawna'],
                data_rejestracji=None if pd.isna(row['data_rejestracji']) else datetime.datetime.strptime(row['data_rejestracji'], '%d.%m.%Y'),
                status=row['status'],
                szerokosc_geo=row['szerokosc_geo'],
                dlugosc_geo=row['dlugosc_geo']
            )
            db.session.add(d)
            db.session.commit()

def load_walne():
    with app.app_context():

        file_path = os.path.join(current_path, 'pkgs/spoldzielnie/src/spoldzielnie/dane/walne.ods')

        df = pd.read_excel(file_path,dtype=str, header=0)



        for index, row in df.iterrows():

            krs = row['krs']
            zera = 10 - len(str(krs))
            krs = '0'*zera + str(krs)     

            def tak_nie(value):
                if pd.isna(value):
                    return None
                value = value.strip().lower()
                if value == 'tak':
                    return True
                elif value == 'nie':
                    return False
                else:
                    return None
                    # raise ValueError(value)


            sprawozdanie_value = tak_nie(row['sprawozdanie_finansowe'])
            uchwala_zatw_value = tak_nie(row['uchwala_zatw'])

            d = Walne(
                spoldzielnia = krs,
                sprawozdanie_finansowe = sprawozdanie_value,
                uchwala_zatw = uchwala_zatw_value,
                kiedy_bylo = None if pd.isna(row['kiedy_bylo']) else datetime.datetime.strptime(row['kiedy_bylo'], '%d-%m-%Y'),
                bilans = row['bilans'],
                uwagi = row['uwagi']

            )
            db.session.add(d)
            db.session.commit()






if __name__ == "__main__":
    print('ehlo')
    load_walne()
    # load_spoldzielnie()
    # load_sprawy()