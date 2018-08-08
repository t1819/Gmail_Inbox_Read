import base64
import sys
import imaplib
import email
import re
import getpass
import datetime
import time
from dateutil.relativedelta import relativedelta

# comment this code if you want to store details in code.
email_address = input('Email Address: ')
password = getpass.getpass()
label = input("Please enter the Gmail label name:")
from_date = input("Please enter the FROM date: ex. 27-Jul-2018\n")
to_date = input("Please enter the TO date. ex.01-Aug-2018\n")

# Uncomment the below code for storing details.
# email_address = "abc@example.com"
# password = "Your password"
# label = "Jenkins"
# from_date = "07-Jul-2018"
# to_date = "30-Jul-2018"

smtp_server = "imap.gmail.com"
smpt_port = 993
subject = []


def filter_date(d1, d2):
    global command

    command = 'SINCE "'+d2+'" BEFORE "'+d1+'"'

def read_emails():
    filter_date(to_date, from_date)
    mail = imaplib.IMAP4_SSL(smtp_server)
    mail.login(email_address, password)
    mail.select('"'+label+'"', readonly=True)
    result, data = mail.uid('search', None, '('+command+')')
    if result == 'OK':
        print('Processing mailbox...')
    else:
        print("Reading error")
        sys.exit(0)
    ids = data[0].split()
    if len(ids) == 0:
        print("No email found in selected dates.")
    for i in ids:
        result, data = mail.uid('fetch', i, "(RFC822)")
        raw_email = data[0]
        f1 = re.split('Subject: ', str(raw_email))
        f2 = re.split(r"\\r", f1[1])
        sub = f2[0]
        subject.append(sub)
    return subject


try:
    subjects = read_emails()
except Exception as e:
    print('[+] Error =' + str(e))
    input("Press enter to exit.")
for i in subject:
    print(i)
    time.sleep(0.2)

input("Press enter to exit.")
