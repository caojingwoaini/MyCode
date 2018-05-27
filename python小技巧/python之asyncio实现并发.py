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











