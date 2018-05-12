#coding:utf-8
#1-10偶数的平方

from functools import reduce



def filter2(map2):
    def filter3(map2_list):
        filter_list=map2(map2_list)
        return list(filter(lambda y:y%2==0,filter_list))
    return filter3

@filter2
def map2(map2_list):
    return list(map(lambda x:x*x,map2_list))

d1=map2(list(range(1,11)))
print(d1)


