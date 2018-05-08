#coding:utf-8

import pymysql
from bs4 import BeautifulSoup
import  urllib.request as urllib2
import re
import codecs
import GetAllLinuxUrlData

class SendForMysql:
    #作用是将这些数据存储到mysql里
    def sendForMysql(self,targetUrl,allLinkData,indexx,dba,cursor):
        str_node = str(allLinkData[indexx])
        soup_node = BeautifulSoup(str_node, "html.parser")
        linux_value = soup_node.get_text()  # linux命令名称
        if r"/linux/" in str_node:
            linux_url = "http://www.runoob.com" + re.split('"', str_node, maxsplit=2)[1]  # 链接
        else:
            linux_url = "http://www.runoob.com/linux/" + re.split('"', str_node, maxsplit=2)[1]  # 链接
        header3 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }
        req_spider3 = urllib2.Request(url=linux_url, headers=header3)
        response_spider3 = codecs.decode(urllib2.urlopen(req_spider3).read(), "UTF-8")
        soup_spider3 = BeautifulSoup(response_spider3, "html.parser")
        allLinkData3 = soup_spider3.find_all("div", class_="article-intro", id="content")[0].find_all('h1')[0].get_text()  # 链接里的简介
        cursor.execute(' select linuxName from asto.linuxTable where linuxName="%s"; ' % linux_value)
        select_result = cursor.fetchall()
        if select_result == ():
            cursor.execute(
                'insert into asto.linuxTable (linuxName,linuxUrl,linuxUrlDes,createAt,updateAt) values ("%s","%s","%s",now(),now());' % (
                linux_value, linux_url, allLinkData3))
            dba.commit()
        else:
            cursor.execute('update asto.linuxTable set updateAt=now() where linuxName="%s"' % linux_value)
            dba.commit()



