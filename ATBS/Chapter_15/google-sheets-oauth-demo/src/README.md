# Google Sheets OAuth Demo (Python)

A clean, beginner-friendly demo project that authenticates with Google OAuth2
(Desktop App flow) and reads/writes data to a Google Spreadsheet using the
Google Sheets API.

This project is designed to be:
- Easy to understand
- Safe to publish on GitHub
- A solid reference for future Google API projects

---

Features
- OAuth2 login (Desktop / Installed App flow)
- Automatic browser-based Google authentication
- Writes demo data to a Google Sheet
- Reads data back and prints it to the terminal
- Automatically detects the first sheet tab (supports non-English names like Φύλλο1)
- Secrets are excluded from version control

---

Project Structure

google-sheets-oauth-demo/
├─ src/
│  └─ main.py
├─ requirements.txt
├─ .gitignore
└─ README.md

---

Requirements
- Python 3.10+
- Google account
- Google Cloud project with:
  - Google Sheets API enabled
  - Google Drive API enabled

---

Google Cloud Setup
1. Create a Google Cloud project
2. Enable Google Sheets API and Google Drive API
3. Configure OAuth Consent Screen
   - User type: External
   - App status: Testing
   - Add your Google account as a Test user
4. Create OAuth Client ID
   - Application type: Desktop app
5. Download credentials and rename to:
   credentials.json

---

Installation

pip install -r requirements.txt

---

Credentials Setup
Place credentials.json in the project root.
On first run, a browser window opens for authentication and creates token.json.

Both files must NOT be committed to GitHub.

---

Usage
Open src/main.py and set your Spreadsheet ID:

SPREADSHEET_ID = "YOUR_SPREADSHEET_ID_HERE"

Run:

python src/main.py

---

Expected Output
- Prints detected sheet tabs
- Writes demo data to A1:D4
- Reads back the same range and prints it

---

Common Issues

Access blocked: App has not completed the Google verification process
- Cause: App is in Testing mode
- Fix: Add your Google account as a Test user

Unable to parse range: Sheet1!A1:D10
- Cause: Sheet tab name is not Sheet1
- Fix: Do not hardcode sheet names

No data found
- Cause: Sheet is empty
- Fix: Add data or run script to write demo data

---

Security
Ensure .gitignore contains:

credentials.json
token.json

---