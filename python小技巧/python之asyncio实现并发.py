#-*- coding:utf-8 -*-

import asyncio
import time

@asyncio.coroutine  #协程
def wget(host):
    print(len(host),host,time.time())

loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]  #要执行的任务
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


"""
返回结果为：
11 www.163.com 1527424493.5807302
15 www.sina.com.cn 1527424493.580792
12 www.sohu.com 1527424493.58081
可以发现，打印出这三个列表的长度都是在同一秒执行的，真正意义上的并发
"""












#coding:utf-8

import asyncio
import time
import  pymysql
import urllib.request as urllib2
import codecs

file=open("E:/火眼风控/性能测试数据/gaodajun.txt","r",encoding="utf-8")
fileContent=file.read()
file.close()
fileContentList=fileContent.split("\n")

@asyncio.coroutine
def tongdunThread(i):
    print(fileContentList[i])


loop=asyncio.get_event_loop()
tasks=[tongdunThread(i) for i in range(4)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#高大俊1,350424195501082038,tt61bbdc859c4ab1a0ec0d2h04e54000,e0a49735aae61c6bdcc99c03a6fa3000
#高大俊2,350424195501082039,tt61bbdc859c4ab1a0ec0d2h04e54001,e0a49735aae61c6bdcc99c03a6fa3001
#高大俊3,350424195501082040,tt61bbdc859c4ab1a0ec0d2h04e54002,e0a49735aae61c6bdcc99c03a6fa3002
#高大俊4,350424195501082041,tt61bbdc859c4ab1a0ec0d2h04e54003,e0a49735aae61c6bdcc99c03a6fa3003


