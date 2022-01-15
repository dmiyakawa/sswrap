from typing import List, Any


class Worksheet:
    def __init__(self):
        self._rows: List[List[Any]] = []

    def get_value(self, row_index: int, col_index: int) -> Any:
        return self._rows[row_index][col_index]
