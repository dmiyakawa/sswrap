#!/usr/bin/env python3

from sswrap.common import from_a1_cell
from sswrap.google import GoogleSpreadsheet


def main():
    # This spreadsheet is maintained by Google, not by us.
    # See also https://developers.google.com/sheets/api/quickstart/python
    ss = GoogleSpreadsheet("1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms")
    sheet = ss["Class Data"]
    d = sheet.get_range_as_dict(*from_a1_cell("A1"), *from_a1_cell("F40"))
    for i, row_d in enumerate(d):
        if not row_d.get("Student Name"):
            break
        print(i, row_d)


if __name__ == "__main__":
    main()
