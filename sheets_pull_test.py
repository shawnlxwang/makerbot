# Install these libraries using pip:
# pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Set up credentials
scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = Credentials.from_service_account_file('google_api_creds.json', scopes=scope)

# Build the service
service = build('sheets', 'v4', credentials=creds)

# Specify the spreadsheet ID and range
spreadsheet_id = '1Ehq7cC-EM0Nc_HvVAeY-cEU5E7T2xqosLwWIMoY4q7s'
range_name = 'Responses!A1:D10'  # Adjust as needed

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get('values', [])

# Print the data
if not values:
    print('No data found.')
else:
    for row in values:
        print(row)