#-*- coding:utf-8 -*-

import asyncio
from functools import reduce
import time
import pymysql

"""
db=pymysql.Connection(host="localhost",db="asto",port=3306,user="root",password="caojing520",charset="utf8")
cursor=db.cursor()
sum=1


while True:
    if sum==30000:
        break
    cursor.execute("insert into StudentMoney(StudentId,StudentMoney) values (%d,%.2f);" % (sum, float(sum)))
    cursor.execute("commit;")
    sum=sum+1

cursor.close()
db.close()
"""