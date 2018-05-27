#-*- coding:utf-8 -*-

import asyncio
from functools import reduce
import time

async def map2(list1):
    number=list(map(lambda x:x*x,list1))
    return number

async def filter2(list1):
    return list(filter(lambda y:y%2==0,list1))

async def reduce2(list1):  #async能够将一个类或方法定义为一个协程
    reduce_list=await map2(list1)  #await关键字的作用是：一个协程里可以启动另外一个协程，并等待它完成返回结果
    number=reduce(lambda a,b:a+b,reduce_list)
    print(number,time.time())
    return number

loop=asyncio.get_event_loop()
tasks=[reduce2(list(range(1,6))),reduce2(list(range(1,11))),reduce2(list(range(1,16)))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
返回结果为:
1240 1527426530.5744839
385 1527426530.574545
55 1527426530.574561
"""




