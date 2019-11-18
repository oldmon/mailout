#!/usr/bin/env python3
import csv,os
maillist='maillist'
files=os.listdir(path=maillist)
for file in files:
    with open(maillist+'/'+file,'r',encoding='utf8')as csvfile:
        rows=csv.reader(csvfile,delimiter='\t')
        for row in rows:
            print(row)
