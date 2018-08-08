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
password = print('Your password: ')+getpass.getpass()
label = input("Please enter the Gmail label name:")
days = input("Read email in between: [new date,old date] [d-m-y,d-m-y] ex.[04-Jun-2018,02-Mar-2018]")

# Uncomment the below code for storing details.
# email_address = "abc@example.com"
# password = "Your password"
# label = "Jenkins"
# days = "07-Jul-2018,31-Jun-2018"

smtp_server = "imap.gmail.com"
smpt_port = 993
subject = []


def filter_date(data):
    global command

    date = days.split(",")
    from_date = date[0]
    to_date = date[1]
    command = 'SINCE "'+to_date+'" BEFORE "'+from_date+'"'


def read_emails():
    filter_date(days)
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


subjects = read_emails()
for i in subject:
    print(i)
    time.sleep(0.2)
