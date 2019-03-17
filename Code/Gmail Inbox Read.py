import base64
import sys
import imaplib
import email
import re
import getpass
import datetime
import time
import config
from dateutil.relativedelta import relativedelta

subject = []


def filter_date(d1, d2):
    global command

    command = 'SINCE "'+d2+'" BEFORE "'+d1+'"'


def read_emails(smtp_server, subject):
    email_address = config.email
    password = config.password
    label = config.label
    from_date = config.from_date
    to_date = config.to_date

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
    for x in ids:
        result, data = mail.uid('fetch', x, "(RFC822)")
        raw_email = data[0]
        f1 = re.split('Subject: ', str(raw_email))
        f2 = re.split(r"\\r", f1[1])
        sub = f2[0]
        subject.append(sub)
    return subject


def main():
    try:
        smtp_server = "imap.gmail.com"
        read_emails(smtp_server, subject)
        return True
    except Exception as e:
        return '[+] Error =' + str(e)


if __name__ == '__main__':
    status = main()
    if status:
        if len(subject) > 0:
            for x in subject:
                print(x)
        print("\nScript run successfully!!")
    input("Press enter to exit.")
    sys.exit(0)

