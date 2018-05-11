#coding:utf-8

import urllib.request as urllib2
import codecs

url="http://www.baidu.com/s?wd="
value="食屎啦你"
url2=url+urllib2.quote(value)
response=codecs.decode(urllib2.urlopen(url2).read(),"utf-8")
print(response)