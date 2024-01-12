import json
import os.path

from functools import lru_cache
from string import Template
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = os.getenv("RANGE_NAME")
TEMPLATE_PATH = "templates/filter_template.siv"
HEADER_PATH = "templates/header.siv"
OUTPUT_PATH = "filters/"


@lru_cache(maxsize=None)
def get_service():
    creds = None
    if os.path.exists("config/token.json"):
        creds = Credentials.from_authorized_user_file("config/token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "config/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("config/token.json", "w") as token:
            token.write(creds.to_json())

    return build("sheets", "v4", credentials=creds)


def main() -> None:
    service = get_service()

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    )
    values = result.get("values", [])

    filters: dict[str, list[str]] = {}

    for row in values[1:]:
        # Print columns A and E, which correspond to indices 0 and 4.
        filter_name = str(row[0])
        email = str(row[1])

        if not filter_name in filters.keys():
            filters[filter_name] = []
        filters[filter_name].append(email)
        print(f'"{email}" added to "{filter_name}"')
        # $EMAIL_ADDRESSES
        # $FILTER_NAME

    for filter_name, emails in filters.items():
        with open(TEMPLATE_PATH, "r") as fp:
            template_content = fp.read()

        template = Template(template_content)
        email_list = json.dumps(emails)
        content = template.substitute(filter_name=filter_name, emails=email_list)
        filepath = f"{OUTPUT_PATH}/{filter_name}.siv"

        with open(HEADER_PATH, "r") as fp:
            header = fp.read()

        with open(filepath, "w+") as fp:
            fp.write("\n".join([header, content]))


if __name__ == "__main__":
    main()
