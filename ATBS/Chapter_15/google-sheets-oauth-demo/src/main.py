from __future__ import annotations

import os.path
from typing import List, Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# If you change scopes, delete token.json and re-run to re-authorize.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_sheets_service() -> Any:
    """
    Creates and returns an authenticated Google Sheets API service.
    Uses OAuth2 (credentials.json) and stores the user token locally (token.json).
    """
    creds = None

    # token.json stores the user's access/refresh tokens.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            # Runs a local server on http://localhost to complete the auth flow.
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w", encoding="utf-8") as token_file:
            token_file.write(creds.to_json())

    return build("sheets", "v4", credentials=creds)


def get_sheet_tabs(service: Any, spreadsheet_id: str) -> List[str]:
    """
    Returns the sheet/tab names in the given spreadsheet.
    """
    meta = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheets = meta.get("sheets", [])
    return [s["properties"]["title"] for s in sheets]


def write_demo_data(service: Any, spreadsheet_id: str, sheet_name: str) -> None:
    """
    Writes a small demo table to A1:D4 on the given sheet.
    """
    values = [
        ["Όνομα", "Μάθημα", "Βαθμός", "Ημερομηνία"],
        ["Papadimitrioudev", "Python + Sheets", 10, "2026-01-30"],
        ["Demo", "Write values", 9, "2026-01-30"],
        ["Test", "Read values", 8, "2026-01-30"],
    ]

    target_range = f"{sheet_name}!A1:D4"

    body = {"values": values}
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=target_range,
        valueInputOption="USER_ENTERED",
        body=body,
    ).execute()


def read_range(service: Any, spreadsheet_id: str, sheet_name: str, a1_range: str) -> List[List[Any]]:
    """
    Reads a range from the spreadsheet and returns values as a 2D list.
    Example a1_range: 'A1:D10'
    """
    full_range = f"{sheet_name}!{a1_range}"
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=full_range,
    ).execute()

    return result.get("values", [])


def main() -> None:
    # Replace with your spreadsheet ID
    spreadsheet_id = "1TU4EaN8MAcAjXX04iIiXnIdA-4Nuc282LPFjRBj4Rkg"

    service = get_sheets_service()

    tabs = get_sheet_tabs(service, spreadsheet_id)
    print(f"Sheet tabs from API: {tabs}")

    if not tabs:
        raise RuntimeError("No sheets/tabs found in this spreadsheet.")

    sheet_name = tabs[0]

    # Write demo data
    write_demo_data(service, spreadsheet_id, sheet_name)
    print(f"✅ Wrote demo data to: {sheet_name}!A1:D4")

    # Read it back
    data = read_range(service, spreadsheet_id, sheet_name, "A1:D10")
    if not data:
        print("No data found in the selected range.")
        return

    print("\n📄 Data read from the sheet:")
    for row in data:
        print(row)


if __name__ == "__main__":
    main()