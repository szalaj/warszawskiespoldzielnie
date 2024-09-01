
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

        range_name = 'sprawy!A:N'
        spreadsheet_id = '1FifjRzyk_igmnqgbQ8qpQDYFPYqvs5QZmDXZRkVy1hY'
        result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])

        df = pd.DataFrame(rows[1:], columns=rows[0])
        # Truncate the table before adding new data
        db.session.execute(text('DELETE FROM sprawa'))
        db.session.commit()
        
        for index, row in df.iterrows():
            krs = row['spoldzielnia_krs'] if not pd.isna(row['spoldzielnia_krs']) else 0
            zera = 10 - len(str(krs))
            krs = '0'*zera + str(krs)

            d = Sprawa(
                spoldzielnia=krs,
                zgloszenie=row['zgloszenie'],
                kontakt=row['kontakt'],
                data_rozpoczenia=None if (pd.isna(row['data_rozpoczenia']) or row['data_rozpoczenia'].strip()=='') else datetime.datetime.strptime(row['data_rozpoczenia'], '%Y-%m-%d'),
                data_zakonczenia=None if (pd.isna(row['data_zakonczenia']) or row['data_zakonczenia'].strip()=='') else datetime.datetime.strptime(row['data_zakonczenia'], '%Y-%m-%d'),
                opis=row['opis'],
                status=row['status'],
                rozwiazanie=row['rozwiazanie'],
                typ = row['typ'],
                temat=row['temat'],
                odnosniki=row['odnosniki'],
                uwagi=row['uwagi'],
                szerokosc_geo=row['szerokosc_geo'],
                dlugosc_geo=row['dlugosc_geo']
            )
            db.session.add(d)
            db.session.commit()

    return rows

if __name__=="__main__":
    rr = read_range()
