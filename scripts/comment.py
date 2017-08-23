#!/bin/python
# Python3 script which continuously reads Gmail messages and uploads them to GitHub
#
# This script assumes there exists a credentials directory (which is .gitignored) containing:
# - oauth secret api key
# - stored oauth access token for the gmail account
# - GitHub personal access token
#
# This also requires:
# - google-api-python-client (can install via pip)

import httplib2
import os
import json
import time
import email
import base64
import requests
import datetime
import traceback

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/gmail.labels'
CLIENT_SECRET_FILE = 'oauth.json'
STORED_CREDENTIAL_FILE = 'stored.json'
CREDENTIAL_DIR = 'credentials'
APPLICATION_NAME = 'Blog Comments'
GMAIL_LABEL = 'blog_comments/needs_upload'

GITHUB_PERSONAL_ACCESS_TOKEN_FILE = 'github_token.txt'
GITHUB_USERNAME = 'wko27'
GITHUB_REPO = 'blog'

POLL_DELAY_SECONDS = 20

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_dir = os.path.relpath(CREDENTIAL_DIR)
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, STORED_CREDENTIAL_FILE)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        client_secret_path = os.path.join(credential_dir, CLIENT_SECRET_FILE)
        flow = client.flow_from_clientsecrets(client_secret_path, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_gmail_service():
    """ Returns Gmail service object """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    return discovery.build('gmail', 'v1', http=http)

def extract_mime_content(mime):
    """Extracts text from message MIME object
    
    Returns:
        String, contents
    """
    if mime.is_multipart():
        for part in mime.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get('Content-Disposition'))
            # skip any text/plain (txt) attachments
            if content_type == 'text/plain' and 'attachment' not in content_disposition:
                body = part.get_payload(decode=True)  # decode
                break
    # not multipart – i.e. plain text, no attachments, keeping fingers crossed
    else:
        body = mime.get_payload(decode=True)
    return str(body, 'utf-8')

def retrieve_parts(message):
    """Extracts subject, from email address, author, and body from a message
    
    Returns:
        dict with post_id, author, email, and comment set
    """
    msg_bytes = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
    msg_str = str(msg_bytes, 'utf-8')
    mime_msg = email.message_from_string(msg_str)

    body = extract_mime_content(mime_msg)
    split = body.split('\n', 1)
    first = split[0]
    author = first[0:first.rfind(':')]
    comment = split[1]

    subject = mime_msg['Subject']
    post_id = subject[len('[blog-comment]:'):]

    from_email = mime_msg['From']
    
    return {
        "post_id": post_id,
        "author": author,
        "email": from_email,
        "comment": comment,
    }

def retrieve_label_id(service):
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    for label in labels:
        if label['name'] == GMAIL_LABEL:
            return label['id']
    raise AssertionError("Could not find label with name " + GMAIL_LABEL)

def check_if_file_exists(token, file):
    commentPath = '_data/{}'.format(file)
    url = 'https://api.github.com/repos/{}/{}/contents/{}'.format(GITHUB_USERNAME, GITHUB_REPO, commentPath)
    r = requests.get(url, auth=(token, ''))
    print(r.status_code)
    print(r.text)
    print(r.json())

def upload_to_github(token, contents):
    payload = {
        'message': "new comment for " + contents['post_id'],
        'author': {
            "name": contents['author'],
            "email": email.utils.parseaddr(contents['email'])[1],
        }
    }
    comment_path = '_data/{}.json'.format(contents['post_id'])
    url = 'https://api.github.com/repos/{}/{}/contents/{}'.format(GITHUB_USERNAME, GITHUB_REPO, comment_path)
    
    comment = {
        "datetime": datetime.datetime.now(timezone.utc).isoformat(),
        "author": contents['author'],
        "comment": contents['comment'].replace('\r', ''),
    }
    
    # Check if file already exists
    r = requests.get(url, auth=(token, ''))
    if r.status_code == 404:
        # Create a new file
        payload['content'] = base64.b64encode(json.dumps([comment]).encode()).decode('utf-8')
        
        r = requests.put(url, data=json.dumps(payload), auth=(token, ''))
        if r.status_code != 201:
            raise AssertionError("Failed to create _data/{}, put request recieved {} error code:\n{}".format(contents['post_id'], r.status_code, r.text))
    elif r.status_code == 200:
        # Append to existing file
        git_file_contents = json.loads(r.content)
        existing = json.loads(base64.b64decode(git_file_contents['content']))
        existing.append(comment)
        
        payload['content'] = base64.b64encode(json.dumps(existing).encode('utf-8')).decode('utf-8')
        payload['sha'] = git_file_contents['sha']
        
        r = requests.put(url, data=json.dumps(payload), auth=(token, ''))
        if r.status_code != 200:
            raise AssertionError("Failed to update _data/{}, post request recieved {} error code:\n{}".format(contents['post_id'], r.status_code, r.text))
    else:
        raise AssertionError("Unable to check if file at {} exists, url: {}".format(comment_path, url))
    
def main():
    """Extracts emails from particular label and uploads the content body to a blog on Git"""
    with open(CREDENTIAL_DIR + '/' + GITHUB_PERSONAL_ACCESS_TOKEN_FILE, 'r') as github_token_file:
        github_token = github_token_file.read().strip()
        
    while True:
        # Retrieve this in a loop in case the token expires
        service = get_gmail_service()
        
        print("Checking for new messages")
        results = service.users().messages().list(userId='me', q='label: ' + GMAIL_LABEL).execute()
        messages = results.get('messages', [])

        if len(messages) > 0:
            gmail_label_id = retrieve_label_id(service)
            for message in messages:
                try:
                    print("Retrieving full message for " + message['id'])
                    message = service.users().messages().get(userId='me', id=message['id'], format='raw').execute()
                    print("Extracting parts of message " + message['id'])
                    comment_parts = retrieve_parts(message)
                    print("Uploading comment from " + message['id'])
                    upload_to_github(github_token, comment_parts)
                    print('Removing label ' + GMAIL_LABEL + ' from message ' + message['id'])
                    service.users().messages().modify(userId='me', id=message['id'], body={"removeLabelIds": [gmail_label_id]}).execute()
                except Exception as e:
                    print("Unable to process message " + message['id'])
                    traceback.print_exc()
                                
        # Sleep for 20 seconds
        print("Finished processing messages, waiting {} seconds before next check".format(POLL_DELAY_SECONDS))
        time.sleep(POLL_DELAY_SECONDS)
    raise AssertionError("Should never get here ...")

if __name__ == '__main__':
    main()
