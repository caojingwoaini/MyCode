#coding:utf-8
"""
该脚步是为了理解mysql里的事务而写的一个小例子
假设银行的数据库有两张表：支票表和储蓄表，现在某个客户A要从其支票账户转移2000元到其储蓄账户，那么至少需求三个步骤：
a.检查A的支票账户余额高于2000元；
b.从A的支票账户余额中减去2000元；
c.在A的储蓄账户余额中增加2000元。
这三个步骤必须要打包在一个事务中，任何一个步骤失败，则必须要回滚所有的步骤，
否则A作为银行的客户就可能要莫名损失2000元，就出问题了。这就是一个典型的事务
"""

import pymysql

db_connection=pymysql.Connection(host="localhost",user="root",password="caojing520",port=3306,db="asto")
cursor=db_connection.cursor()
cursor.execute(" SELECT * FROM asto.haha; ")
data1=cursor.fetchall();


companyA=data1[0][1]  #客户A
companyB=data1[1][1]  #客户B　

if companyA>2000:
    cursor.execute(" start transaction; ")
    cursor.execute(" update asto.haha set price=%d-2000 where id=1 " % companyA) # 客户A减少2000
    cursor.execute(" SELECT price FROM asto.haha where id=1; ")
    data2=cursor.fetchall()[0][0]  # 客户A减少2000之后的结果
    if companyA-2000==data2:
        cursor.execute(" update asto.haha set price=%d+2000 where id=2 " % companyB)  #客户B增加2000
        cursor.execute(" SELECT price FROM asto.haha where id=2; ")
        data3=cursor.fetchall()[0][0]  # 客户B增加2000之后的结果
        if companyB+2000==data3:
            cursor.execute(" commit; ")
            print(" 转账操作完成")
        else:
            cursor.execute(" rollback; ")
            print("由于客户B的账户余额并没有多出2000，所以此次交易不成立")
    else:
        cursor.execute(" rollback; ")
        print("由于客户A的账户余额并没有减少2000，所以此次交易不成立")
else:
    print("客户A的账户余额少于2000，无法转账　")

cursor.close();
db_connection.close()
