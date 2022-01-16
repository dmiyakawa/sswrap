import os.path
from typing import List, Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from sswrap.exceptions import SswrapException
from sswrap.spreadsheet import Spreadsheet
from sswrap.worksheet import Worksheet


def prepare_sheets_service(*,
                           scopes: List[str] = ["https://www.googleapis.com/auth/spreadsheets.readonly"],
                           credential_path: str = "credentials.json",
                           token_path: str = "token.json"):
    # Based on https://developers.google.com/sheets/api/quickstart/python
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, scopes)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credential_path, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, "w") as token:
            token.write(creds.to_json())
    if not creds:
        raise SswrapException("Failed to create a credential for Google Sheets API")

    service = build("sheets", "v4", credentials=creds)
    return service


class GoogleSpreadsheet(Spreadsheet):
    def num_worksheets(self) -> int:
        pass

    def __getitem__(self, index: int) -> Worksheet:
        pass

    def __len__(self) -> int:
        pass


class GoogleWorksheet(Worksheet):
    def get_value(self, row_index: int, col_index: int) -> Any:
        pass


def _run_smoke_test():
    """\
    Runs a simple procedure demonstrating Google Sheets API.
    See also https://developers.google.com/sheets/api/quickstart/python
    """
    service = prepare_sheets_service()
    sheet = service.spreadsheets()
    # Note this spreadsheet is maintained by Google, not by us.
    result = sheet.values().get(spreadsheetId="1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms",
                                range="Class Data!A2:E").execute()
    values = result.get("values", [])

    if not values:
        print("No data found.")
        return

    print("Name, Major:")
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print(f"{row[0]}, {row[4]}")


if __name__ == "__main__":
    print("Start running an embedded smoke test")
    _run_smoke_test()
