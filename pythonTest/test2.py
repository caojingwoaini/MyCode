#-*- coding:utf-8 -*-

import asyncio
from functools import reduce
import time
import pymysql
from selenium import webdriver

@asyncio.coroutine
def wget(host):
    print(len(host),host,time.time())

loop=asyncio.get_event_loop()
task=[wget(i) for i in ["www.baidu.com","www.geogle.com","www.taobao.com"]]
loop.run_until_complete(asyncio.wait(task))