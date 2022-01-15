from typing import Any, List

from sswrap.worksheet import Worksheet


class WritableWorksheet(Worksheet):
    def __init__(self):
        super().__init__()

    @property
    def rows(self) -> List[List[Any]]:
        return self._rows

    def set_value(self, row_index: int, col_index: int, value: Any):
        self._rows[row_index][col_index] = value
