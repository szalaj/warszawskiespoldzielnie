
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

        range_name = 'walne!A:G'
        spreadsheet_id = '1FifjRzyk_igmnqgbQ8qpQDYFPYqvs5QZmDXZRkVy1hY'
        result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])

        df = pd.DataFrame(rows[1:], columns=rows[0])
        # Truncate the table before adding new data
        db.session.execute(text('DELETE FROM walne'))
        db.session.commit()
        
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


            uchwala_zatw_value = tak_nie(row['uchwala_zatw'])

            d = Walne(
                spoldzielnia = krs,
                rok = int(row['rok_kalendarzowy']),
                uchwala_zatw = uchwala_zatw_value,
                kiedy_bylo = None if (pd.isna(row['kiedy_bylo']) or row['kiedy_bylo'].strip()=='') else datetime.datetime.strptime(row['kiedy_bylo'], '%d-%m-%Y'),
                bilans = None if (pd.isna(row['bilans']) or row['bilans'].strip()=='') else row['bilans'].replace(',',''),
                uwagi = row['uwagi']

            )
            db.session.add(d)
            db.session.commit()

    return rows

if __name__=="__main__":
    rr = read_range()
