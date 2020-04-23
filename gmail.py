import httplib2
import os
import oauth2client
from oauth2client import client, tools, file
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'FPSU_Gmail'


def get_credentials():
    home_dir = os.path.expanduser('/var/www/FPSU/FPSU/alg252kjaglasj/')
    credential_dir = os.path.join(home_dir, 'credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'gmail-python-email-send.json')
    print credential_path
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials


def create_message(to, subject, msgHTML):
    #msg = MIMEText(msgPlain)

    msg = MIMEMultipart('alternative')

    msg['Subject'] = subject
    msg['From'] = 'codingprivacy123@gmail.com'
    msg['To'] = to

    msg.attach(MIMEText(msgHTML, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_string())
    raw = raw.decode()
    body = {'raw': raw}
    return body


def send_message_internal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        # print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def send_message(to, subject, msgPlain):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message_final = create_message(to, subject, msgPlain)
    send_message_internal(service, "me", message_final)
