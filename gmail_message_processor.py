from googleapiclient.discovery import build
from gmail_api_auth import authenticate_gmail_api
from gmail_label_manager import get_label_id_by_name

def fetch_emails_by_label(label_name):
    creds = authenticate_gmail_api()
    service = build('gmail', 'v1', credentials=creds)
    label_id = get_label_id_by_name(label_name)
    if label_id is None:
        print(f'Label {label_name} not found.')
        return []

    response = service.users().messages().list(userId='me', labelIds=[label_id]).execute()
    messages = response.get('messages', [])
    return messages
