#-*- coding:utf-8 -*-
#该脚步是监控mysql某个字段，每隔多少秒去检查一次，如果该字段被修改成了所预期的结果，则能够执行其他方法

import time
import pymysql



startTime=time.time()

def dd():
    time_sum=0
    while True:
        db = pymysql.connect(host="localhost", user="root", password="caojing520", charset="utf8", port=3306, db="asto")
        cursor = db.cursor()
        cursor.execute(" select * from asto.grade where idgrade=12; ")
        data=cursor.fetchall()[0][3]
        print(data)
        if data==100 or time_sum>=20:
            break
        time.sleep(5)
        time_sum=time_sum+5
        cursor.close()
        db.close()
    return data

def Print():
    print("hello world")

j1=dd()
endTime=time.time()
print(endTime-startTime)

if j1==100:
    Print()