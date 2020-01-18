import os.path
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']    
BASE = os.path.dirname(os.path.abspath(__file__))
data = json.loads(open(os.path.join(BASE, "client_secret.json")).read())
creds = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)
client = gspread.authorize(creds)
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1-TxF0p273SPv7XI67SUJCw-oaCxHnYk1CUTRaYJj5Nc/edit#gid=0&fvid=1259069163')