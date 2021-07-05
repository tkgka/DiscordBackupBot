from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './json/keys.json'
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
def typeToSpreadSheed(value):
    SAMPLE_SPREADSHEET_ID = 'SHEET_ID'
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    # sheet = service.spreadsheets()
    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="test!A1:C3").execute()
    aoa = value
    
    result = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="test2!B2",valueInputOption="USER_ENTERED", body={'values':aoa}).execute()

    