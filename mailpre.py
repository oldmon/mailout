#!/usr/bin/env python3
import csv
import os
MAIL_LIST = 'maillist'
for file in os.listdir(path=MAIL_LIST):
    with open(MAIL_LIST+'/'+file, 'r', encoding='utf8')as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            org = row[3]
            name = row[2]
            if row[1]:
                mailto = row[1]
            else:
                mailto = row[0]
            print(mailto+','+name)
