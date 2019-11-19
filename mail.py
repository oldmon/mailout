#!/usr/bin/env python3
import csv,os
maillist='maillist'
files=os.listdir(path=maillist)
for file in files:
    with open(maillist+'/'+file,'r',encoding='utf8')as csvfile:
        rows=csv.reader(csvfile)
        for row in rows:
            org=row[3]
            name=row[2]
            if row[1]:
                mailto=row[1]
            else:
                mailto=row[0]
            print("來自"+org+"的"+name+"的email是"+mailto)
