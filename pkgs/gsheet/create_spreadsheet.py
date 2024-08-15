
from auth import spreadsheet_service
from auth import drive_service

def create():
    spreadsheet_details = {
        'properties': {
            'title': 'Test Spreadsheet'
        }
    }
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details).execute()

    sheetId = sheet.get('spreadsheetId')
    print(f'Spreadsheet ID: {sheetId}')
    permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': 'mszalajski@gmail.com'
    }
    drive_service.permissions().create(fileId=sheetId, body=permission).execute()
    return sheetId

create()