from dataclasses import dataclass
import gspread
from model import Status, Emailer, Email, unify
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.discovery import build

@dataclass
class Submission(Emailer):
    email: str
    name: str
    requested_status: str
    email_board: str
    claimed_status: int

    @staticmethod
    def parse(value):
        status = "submission"
        if value[8] != "":
            status = "candidate"
        if value[9] != "":
            status = "support"
        if value[10] != "":
            status = "normal"

        claimed_status = -1
        if value[13] == "zwyczajny":
            claimed_status = 1
        elif value[13] == "wspierający":
            claimed_status = 2
        elif value[13] == "rezygnacja":
            claimed_status = 4
        else:
            if value[13] != "":
                raise ValueError("Invalid value for claimed_status: {}, for {}".format(value[12], value))

        return Submission(unify(value[2]), value[3], status, value[11], Status(claimed_status))
    
    def emails(self) -> list[Email]:
        return [self.email]

    
    @staticmethod
    def empty(value):
        return all([v == '' for v in value[1:]])
    

def credentials():
    # Replace 'path/to/your/credentials.json' with the path to your Google Sheets API credentials JSON file
    # TODO add information how to provide credentials
    credentials_path = './credentials/google.json'
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    return ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
 

def list_column_values(spreadsheet_key, sheet_name):
    gc = gspread.authorize(credentials())

    try:
        # Open the spreadsheet and select the worksheet
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(sheet_name)

        worksheet.get_values

        # Get all values in the specified column
        column_values = worksheet.get_all_values()

        # Print the values
        return [Submission.parse(value) for value in column_values[2:] if not Submission.empty(value)]

    except gspread.exceptions.SpreadsheetNotFound:
        print("Spreadsheet not found.")
    except gspread.exceptions.WorksheetNotFound:
        print("Worksheet not found.")

def submissions():
    # Identifier of the submissions file
    spreadsheet_key = '1Wop0j4pNMjpXxhNKkzvAvEzD84BeQsDnSxqRfxgAw3o'
    sheet_name = 'Kadry'

    return list_column_values(spreadsheet_key, sheet_name)

  
def list_members(group_email) -> list[str]:
    # Build the service
    service = build('admin', 'directory_v1', credentials=credentials())
    # Retrieve members of the group
    response = service.members().list(groupKey=group_email).execute()
    # Print out the email addresses of the members
    return response['members']

def main():
    for s in submissions():
        action = s.needs_action()
        if len(action) > 0:
            print("Needed action {} for {}", action, s)


if __name__ == "__main__":
    main()