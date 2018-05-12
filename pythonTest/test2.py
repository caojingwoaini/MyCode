#coding:utf-8


import time
from functools import reduce

def deco(func):
    def wrapper(a,b):
        startTime=time.time()
        func(a,b)
        endTime=time.time()
        msecs=(endTime-startTime)*1000
        print(msecs)
    return wrapper

@deco
def func(a,b):
    print(a)
    time.sleep(1)
    print(b)

if __name__ == "__main__":
    f=func
    f("hello","python")






