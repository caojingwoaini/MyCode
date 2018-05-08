#coding:utf-8

import GetAllLinuxUrlData,SendForMysql
import pymysql


class LinuxSpiderControl(object):
    def __init__(self):
        self.getAllLinuxUrlData=GetAllLinuxUrlData.GetAllLinuxUrlData()
        self.sendForMysql=SendForMysql.SendForMysql()

    #爬虫运行方法
    def spiderRun(self,targetUrl):
        allLinkData = GetAllLinuxUrlData.GetAllLinuxUrlData().getAllLinuxUrlData(targetUrl)
        count_spider = len(allLinkData)
        indexx = 0
        # 插入或更新数据库
        dba = pymysql.Connection(host="localhost", db="asto", port=3306, user="root", password="caojing520",
                                 charset="utf8")
        cursor = dba.cursor()
        while count_spider > 0:
            self.sendForMysql.sendForMysql(targetUrl,allLinkData,indexx,dba,cursor)
            count_spider = count_spider - 1
            indexx = indexx + 1

        cursor.close()
        dba.close()


if __name__ == "__main__":
    targetUrl="http://www.runoob.com/linux/linux-command-manual.html"
    contronl_spider=LinuxSpiderControl()
    contronl_spider.spiderRun(targetUrl)



