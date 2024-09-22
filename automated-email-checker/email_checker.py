import os # standard lib for interacting with os, specifically for reading env var
import time # standardllib to work with time, used for filtering emails by time

from dotenv import load_dotenv # allows us to load env vars from .env file
from google.oauth2.credentials import Credentials # manage Oauth2 creds
from google_auth_oauthlib.flow import InstalledAppFlow # facilitates oauth2 flow for user auth
from google.auth.transport.requests import Request # used to refresh cred if they have expired
from googleapiclient.discovery import build # this will let us interact with gmail api
from gpt_utils import summarize_and_rank_emails

# load env var from the .env file
# file contains sensitive info like the path to the oauth2 creds file
load_dotenv()

# retreive the path to the outh2 client secret json file from .env file
# file contains client ID and secret for auth with google
CLIENT_SECRET_FILE = os.getenv('CLIENT_SECRET_FILE')

# define the Oauth2 scope for read-only gmail access
# 'https://www.googleapis.com/auth/gmail.readonly' grants read-only access to the Gmail account
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_email_services():
    """Authenticate the user and get the Gmail API service using OAuth2."""

    creds = None # this will hold our OAuth2 creds
    token_file = 'token.json' # file to store the user's access and refresh tokens

    # step 1: check if the token file already exists (creds already stored)
    if os.path.exists(token_file):
        # if the token file exists, load the creds from it
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    # step 2: if no valid creds exists or expired, need to authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # refresh the creds if they have expired
            creds.refresh(Request())
        else:
            # if no valid creds exist, start the Oauth authentication flow
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0) # runs a local server for the OAuth2 callback

        # save the new creds for future use
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    # step 3: return the authenticated gmail api service object
    return build('gmail', 'v1', credentials=creds)

def list_emails_by_date(service, query_date, use_gpt=False):
    """List all emails from the Primary inbox, filtering by the specified date."""
    
    # Use Gmail API query to search for emails after the 'query_date' in the Primary inbox
    query = f"after:{query_date} -category:social -category:promotions"

    # Initialize variables to handle pagination
    messages = []
    next_page_token = None

    # Keep fetching emails until there are no more pages
    while True:
        # Fetch emails from the Inbox, excluding Social and Promotions categories
        results = service.users().messages().list(
            userId='me',
            q=query,
            labelIds=['INBOX'],  # Filter for all emails in the Inbox
            pageToken=next_page_token
        ).execute()

        # Add the new messages to the list of all messages
        messages.extend(results.get('messages', []))

        # Check if there's another page of results (pagination)
        next_page_token = results.get('nextPageToken')

        # Break the loop if there are no more pages
        if not next_page_token:
            break

    # Step 4: Print messages if found, otherwise notify that none were found
    if not messages:
        print(f"No messages found after {query_date} in the Primary inbox")
    else:
        # Prepare a list of email subjects and snippets to pass to GPT (if requested)
        email_summaries = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            subject = msg.get('snippet')
            snippet = msg.get('snippet', 'No snippet available')
            email_summaries.append({"subject": subject, "snippet": snippet})

            # Print a snippet of each email
            print("\n")
            print(f"Subject: {subject}\n")
        
        # Optional: GPT summarization and ranking
        if use_gpt:
            report = summarize_and_rank_emails(email_summaries)
            print("\nGPT Summary and Ranking of Emails:")
            print(report)
