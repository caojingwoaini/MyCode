#coding:utf-8

import urllib.request as urllib2
from bs4 import BeautifulSoup
import urllib.parse
import codecs
import re
import pymysql

url2="http://www.runoob.com/linux/linux-command-manual.html"
header2={
"Accept-Encoding":"*",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Connection":"keep-alive",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
req_spider=urllib2.Request(url=url2,headers=header2)
response_spider=codecs.decode(urllib2.urlopen(req_spider).read(),"UTF-8")


soup_spider=BeautifulSoup(response_spider,"html.parser");
allLinkData=soup_spider.find_all("a",target="_blank",href=re.compile(r".*linux-comm-\w+.html"))  #所有Linux命令的url




count_spider=len(allLinkData)
indexx=0
#插入或更新数据库
dba = pymysql.Connection(host="localhost", db="asto", port=3306, user="root", password="caojing520",charset="utf8")
cursor = dba.cursor()
while count_spider>0:
    #print(allLinkData[indexx])
    str_node=str(allLinkData[indexx])
    soup_node=BeautifulSoup(str_node,"html.parser")
    linux_value=soup_node.get_text() #linux命令名称
    if r"/linux/" in str_node:
        linux_url="http://www.runoob.com"+re.split('"',str_node,maxsplit=2)[1] #链接
    else:
        linux_url="http://www.runoob.com/linux/"+re.split('"',str_node,maxsplit=2)[1] #链接
    header3={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
    req_spider3=urllib2.Request(url=linux_url,headers=header3)
    response_spider3=codecs.decode(urllib2.urlopen(req_spider3).read(),"UTF-8")
    soup_spider3=BeautifulSoup(response_spider3,"html.parser")
    allLinkData3=soup_spider3.find_all("div",class_="article-intro",id="content")[0].find_all('h1')[0].get_text() #链接里的简介



    cursor.execute(' select linuxName from asto.linuxTable where linuxName="%s"; ' % linux_value)
    select_result = cursor.fetchall()
    if select_result == ():
        cursor.execute(
            'insert into asto.linuxTable (linuxName,linuxUrl,linuxUrlDes,createAt,updateAt) values ("%s","%s","%s",now(),now());' % (linux_value,linux_url,allLinkData3))
        dba.commit()
    else:
        cursor.execute('update asto.linuxTable set updateAt=now() where linuxName="%s"' % linux_value)
        dba.commit()



    count_spider=count_spider-1
    indexx=indexx+1
    print(linux_value)

cursor.close()
dba.close()







