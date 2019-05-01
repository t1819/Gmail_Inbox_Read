import sys
import imaplib
import re
import time
import config
'''
    Description: Read your Gmail label for specific duration and print all subjects.
    Pre-requirements: Go to google account --> security --> enable "Less secure app access" option.
    Use: set options in config.py file before using this script.
'''


class EmailRead:
    def read_emails(self):
        try:
            mail = imaplib.IMAP4_SSL(self.smtp_server)
            mail.login(self.email_address, self.password)
            mail.select(self.label, readonly=True)
            result, data = mail.uid('search', None, self.command)
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
                self.subject.append(sub)
            return self.subject
        except:
            print("[+] Error in reading your %s label." % self.label)

    def __init__(self):
        self.subject = []
        self.smtp_server = "imap.gmail.com"
        self.email_address = config.email
        self.password = config.password
        self.label = '"'+config.label+'"'
        self.from_date = config.from_date
        self.to_date = config.to_date
        self.command = '(SINCE "' + self.from_date + '" BEFORE "' + self.to_date + '")'


if __name__ == '__main__':
    r1 = EmailRead()
    data = r1.read_emails()
    if len(data) > 0:
        for i in data:
            print(i)
            time.sleep(.2)
