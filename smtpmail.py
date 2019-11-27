#!/usr/bin/env python3
'''
For email out with specific maillist format
'''
import csv
import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'service@sync.cloudbox.hinet.net'
subject = 'hicloud box(e)功能發佈'
fromname = 'hicloud box(e)'

if len(sys.argv) != 3:
    print("Usage: python3 "+sys.argv[0]+" MAILLIST MAILCONTENT")
    sys.exit()

MAILLIST = sys.argv[1]
CONTENT = sys.argv[2]
with open(CONTENT, 'r', encoding='utf8')as f:
    MESG = f.read()

with open(MAILLIST, 'r', encoding='utf8')as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        name = row[1]
        receivers = row[0]

        message = MIMEText(MESG, 'plain', 'utf-8')
        message['From'] = Header(fromname, 'utf-8')
        message['To'] = Header(name, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP('www.hibox.hinet.net')
            smtpObj.login('service@sync.cloudbox.hinet.net', 'coidc805')
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("郵件發送成功")
        except smtplib.SMTPException:
            print("Error: 無法發送郵件")

        time.sleep(8)
