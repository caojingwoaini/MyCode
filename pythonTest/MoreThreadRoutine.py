#coding:utf-8
#该代码是为了理解多线程并发（3个线程）来理解mysql事务的样例

import asyncio
import time
import pymysql

@asyncio.coroutine
def payMoney():
    db=pymysql.Connection(host="localhost",db="asto",port=3306,user="root",password="caojing520",charset="utf8")
    cursor=db.cursor()

    cursor.execute(" select StudentMoney from StudentMoney  where StudentId=1 ")
    studentMoney1=float(cursor.fetchall()[0][0])

    cursor.execute("begin;")
    cursor.execute("update StudentMoney t2 set t2.StudentMoney=t2.StudentMoney-500 where t2.StudentId=(select t1.idstudent from student t1 where t1.name='高坤');")
    cursor.execute("update StudentMoney t2 set t2.StudentMoney=t2.StudentMoney+500 where t2.StudentId=(select t1.idstudent from student t1 where t1.name='徐震');")

    if studentMoney1>0:
        cursor.execute("commit;")
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),"执行转账事务成功")
    else:
        cursor.execute("rollback;")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"执行转账事务失败并回滚")
    cursor.close()
    db.close()


loop=asyncio.get_event_loop()
tasks=[payMoney() for i in range(3)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()