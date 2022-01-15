from typing import List

from sswrap.worksheet import Worksheet


class Spreadsheet:
    """
    A spreadsheet that may contain multiple worksheets.
    Note that a spreadsheet built from a CSV file just contains a single worksheet, while
    one from an Excel or Google Sheets can contain multiple worksheets.
    """
    def __init__(self):
        self._worksheets: List[Worksheet] = []

    def num_worksheets(self) -> int:
        return len(self._worksheets)

    def __getitem__(self, index: int):
        return self._worksheets[index]
