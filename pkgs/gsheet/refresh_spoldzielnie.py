
from auth import spreadsheet_service
from auth import drive_service
from spoldzielnie import init_app , db
from spoldzielnie.models import Spoldzielnia, Sprawa, Walne
import pandas as pd
import datetime
from sqlalchemy.sql import text

# spoldzielnie_mieszkaniowe : 1FifjRzyk_igmnqgbQ8qpQDYFPYqvs5QZmDXZRkVy1hY

app=init_app()


def read_range():
    with app.app_context():

        range_name = 'spoldzielnie!A:M'
        spreadsheet_id = '1FifjRzyk_igmnqgbQ8qpQDYFPYqvs5QZmDXZRkVy1hY'
        result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])

        df = pd.DataFrame(rows[1:], columns=rows[0])
        # Truncate the table before adding new data
        db.session.execute(text('DELETE FROM spoldzielnia'))
        db.session.commit()
        

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
                data_rejestracji=None if (pd.isna(row['data_rejestracji']) or row['data_rejestracji'].strip()=='')  else datetime.datetime.strptime(row['data_rejestracji'], '%d.%m.%Y'),
                status=row['status'],
                szerokosc_geo=row['szerokosc_geo'],
                dlugosc_geo=row['dlugosc_geo']
            )
            db.session.add(d)
            db.session.commit()

    return rows

if __name__=="__main__":
    rr = read_range()
