#-*- coding:utf-8 -*-



from io import  StringIO

from functools import reduce
from itertools import groupby

list1=[["caojing",13],
["caojing",144],
["caojing",66],
["gaokun",54],
["gaokun",900],
["fanyanwei",250]]

#for k,v in groupby(list1,lambda x:x[0]):
#    print(k,list(v))
print(list(reduce(lambda x,y:[row1,x[1]+y[1]],row2) for row1,row2 in groupby(list1,lambda z:z[0])))
