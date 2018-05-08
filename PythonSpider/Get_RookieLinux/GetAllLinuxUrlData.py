#coding:utf-8

import urllib.request as urllib2
import codecs
from bs4 import BeautifulSoup
import re

class GetAllLinuxUrlData:
    #获取该url界面上的所有url数据
    def getAllLinuxUrlData(self,targetUrl):
        header2 = {
            "Accept-Encoding": "*",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Connection": "keep-alive",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }
        req_spider = urllib2.Request(url=targetUrl, headers=header2)
        response_spider = codecs.decode(urllib2.urlopen(req_spider).read(), "UTF-8")
        allLinkData=self.parserLinuxUrlData(response_spider)  #所有的url数据
        return allLinkData

    #解析出所有linux的url
    def parserLinuxUrlData(self,response_spider):
        soup_spider = BeautifulSoup(response_spider, "html.parser");
        allLinkData = soup_spider.find_all("a", target="_blank",href=re.compile(r".*linux-comm-\w+.html"))  # 所有Linux命令的url
        return allLinkData







