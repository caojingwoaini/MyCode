#-*- coding:utf-8 -*-
#使用装饰器来解决这个问题，装饰器函数应该写在类外面
#该例子中，self也是一个参数，所以要在装饰器方法里带上参数self

from functools import reduce


def map_filter(sum2):
    def map_filter2(self,sum2_list):
        sum2_value = sum2(self,list(map(lambda c: c * c, list(filter(lambda d: d % 2 == 0, sum2_list)))))
        return sum2_value
    return map_filter2

class Test2(object):

    @map_filter
    def sum2(self,sum2_list):
        return reduce(lambda a,b:a+b,sum2_list)
if __name__ == '__main__':
    j1=Test2()
    list1=list(range(1,11))
    print(j1.sum2(list1))






