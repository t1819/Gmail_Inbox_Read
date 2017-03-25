#Read your inbox email and automate the boring stuff.

import base64, imaplib, email, re
imaplib._MAXLINE = 400000

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "username" + ORG_EMAIL
FROM_PWD    = "password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

Ondate = input('Please enter date[Date Month Year] :\n')

def read_email_from_gmail():
 mail = imaplib.IMAP4_SSL(SMTP_SERVER)
 mail.login(FROM_EMAIL,FROM_PWD)
 mail.select('INBOX', readonly=True)

 type, data = mail.search(None, "ALL")
 mail_ids = data[0]
 count = 0

 id_list = mail_ids.split()
 latest_email_id = int(id_list[-1])
 first_email_id = int(latest_email_id - 100)

 for i in range(latest_email_id,first_email_id, -1):
     if i == latest_email_id:
         typ, data = mail.fetch(str(i), '(RFC822)')
         if typ == 'OK':
             for response_part in data:
                 if isinstance(response_part, tuple):
                     raw_email = email.message_from_bytes(response_part[1])
                     encrypt = re.search("base64",str(raw_email))
                     if encrypt:
                         f1 = re.split('(base64*)', str(raw_email))
                         msg = base64.b64decode(f1[2])
                         if re.search(Ondate, raw_email['date']):
                             # print(raw_email)
                             # whatever you want to search. Complete email value store in [raw_email] varible.
                             count += 1
                     else:
                         raw_email = email.message_from_bytes(response_part[1])
                         if re.search(Ondate, raw_email['date']):
                             # whatever you want to search. Complete email value store in [raw_email] varible.
                             # print(raw_email)
                             count += 1
         else:
             print("Issue detected in email reading")

 print(str("Wow, Script Executed successfully. Total Number of emails read: " + str(count)))

read_email_from_gmail()
