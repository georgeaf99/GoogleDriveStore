import gspread

class Store:
    def __init__(self, spreadsheet_id, credentials, worksheet_num=0):
        self._gspread_client = gspread.authorize(credentials)

        spreadsheet = self._gspread_client.open_by_key(spreadsheet_id)
        self._worksheet = spreadsheet.get_worksheet(worksheet_num)

        # The first row of the spreadsheet serves as the schema
        self.schema = self._worksheet.row_values(1)

    def get(self, index):
        # NOTE : this returns the schema if index is 0
        row = self._worksheet.row_values(index)

        # Ignore empty values
        return {c,v for c,v in zip(schema, row) if v != ''}

    def push(self, data):
        row = [data.get(c) or '' for c in row]

        self._worksheet.append_row(values)

        # TODO : return an index

    def update(self, index, data):
        updated = [data.get(c) for c in row]
        
        cells = self._worksheet.range(
            first_row=index,
            first_col=1,
            last_row=index,
            last_col=1+len(self.schema)
        )

        for new, old in zip(updated, cells):
            if new:
                old.value = new
        
        self._worksheet.update_cells(cells)

    def delete(self, index):
        pass

if __name__ == "__main__":
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    store = Store("foobar", credentials)
