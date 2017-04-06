import gspread

class Store:
    def __init__(self, spreadsheet_id, credentials):
        self._gspread_client = gspread.authorize(credentials)
        self._spreadsheet = self._gspread_client.open_by_key(spreadsheet_id)

    def get(self, index):
        pass

    def push(self, data):
        pass

    def update(self, index, data):
        pass

if __name__ == "__main__":
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    store = Store("foobar", credentials)
