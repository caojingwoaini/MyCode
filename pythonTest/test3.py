#-*- coding:utf-8 -*-

from functools import reduce

def log(func):
    def wrapper(self):
        print('log')
        func(self)
    return wrapper


class Test():
    @log
    def hello(self):
        print('hello')

t = Test()
t.hello()