
from auth import spreadsheet_service
from auth import drive_service

# spoldzielnie_mieszkaniowe : 1FifjRzyk_igmnqgbQ8qpQDYFPYqvs5QZmDXZRkVy1hY

def read_range():
    range_name = 'walne!A:C'
    spreadsheet_id = '1FifjRzyk_igmnqgbQ8qpQDYFPYqvs5QZmDXZRkVy1hY'
    result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    return rows

if __name__=="__main__":
    rr = read_range()
    print(len(rr))