import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
load_dotenv()

class GSheet:
    scope =  ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('G_SERVICE_CRED'), scope)
    client = gspread.authorize(creds)
    sheet = client.open("dengdeng-labels").sheet1

    def getAll(self):
        return self.sheet.get_all_records()

if __name__ == "__main__":
    gs = GSheet()
    all = gs.getAll()
    print(all)