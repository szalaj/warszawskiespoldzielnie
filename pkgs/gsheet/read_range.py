
from auth import spreadsheet_service
from auth import drive_service

def read_range():
    range_name = 'Arkusz1!A:D'
    spreadsheet_id = '1jY36U5vTLooXMUbUvk9sgOStmF6y2pujMaDF9Rtca4g'
    result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    return rows

print(read_range())