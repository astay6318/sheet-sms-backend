# Django Google Sheets Integration with Twilio Notifications

This Django project facilitates the collection of user responses to a form, updating a corresponding spreadsheet, and sending notifications via Twilio. Signals are employed to ensure that model changes are not required when sending SMS notifications.

## Features

- Collects user responses to a form
- Updates a Google Spreadsheet with user responses
- Sends notifications to the client via Twilio

## Tech Stack

- Django
- Google API (Google Sheet API, Google Drive API)
- Twilio API

## Getting Started

### Prerequisites

Ensure you have the following prerequisites installed:

- Python
- Virtualenv (optional but recommended)

### Installation and Configuration

```bash
# Clone the repository:
git clone https://github.com/your-username/your-project.git       
cd your-project       
```
# Set up and activate a virtual environment:
```
python -m venv venv       
source venv/bin/activate          # On Windows, use `venv\Scripts\activate`  
```

# Install dependencies:
```
pip install -r requirements.txt     
```
# Copy the provided example.env to create a new .env file.

## Set up Google API:
- Create a project on the Google Cloud Platform.
- Enable Google Sheet API and Google Drive API.
- Create credentials, download the JSON key, and add it to the .env file.
- Open an untitled Google Sheet and give access to the user mentioned in the JSON key.
- Update the json_file_path in signals.py with the name of the downloaded API key.
- Find the sheet ID as depicted in the instructions.

# Set up Twilio:
- Obtain twilio_account_sid and auth_token by creating an account on the Twilio official website.
- Use these credentials in the .env file.


