from sswrap import Spreadsheet


class WritableSpreadsheet(Spreadsheet):
    def __init__(self):
        super().__init__()

    def add_worksheet(self) -> "WritableWorksheet":
        from sswrap import WritableWorksheet
        ws = WritableWorksheet()
        self._worksheets.append(ws)
        return ws
