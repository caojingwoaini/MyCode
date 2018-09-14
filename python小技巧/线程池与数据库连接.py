#coding:utf-8

import asyncio
import  pymysql
import urllib.request as urllib2
import time
import threading
from DBUtils.PooledDB import PooledDB,SharedDBConnection

file=open("E:/火眼风控/性能测试数据/gaodajun2.txt","r",encoding="utf-8")
fileContent=file.read()
file.close()
fileContentList=fileContent.split("\n")

POOL=PooledDB(
    creator=pymysql,   #使用链接数据库的模块
    maxconnections=1000,  #连接池允许的最大连接数，0和None表示没有限制
    mincached = 2, #初始化时，连接池至少创建的空闲的连接，0表示不创建
    maxcached = 5, #连接池空闲的最多连接数，0和None表示没有限制
    maxshared = 1000, #连接池中最多共享的连接数量，0和None表示全部共享，ps:其实并没有什么用，因为pymsql和MySQLDB等模块中的threadsafety都为1，所有值无论设置多少，_maxcahed永远为0，所以永远是所有链接共享
    blocking = True, #链接池中如果没有可用共享连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
    setsession = [],#开始会话前执行的命令列表
    ping = 0,#ping Mysql 服务端，检查服务是否可用
    host = '192.168.5.154',
    port = 3306,
    user = 'dt',
    password = 'dtonly',
    database = 'data_transport',
    charset = 'utf8'
)

def tongdunThread(i):
    #步骤一：调同盾贷前接口
    fileContent=fileContentList[i]
    partyName=fileContent.split(",")[0]
    idCard=fileContent.split(",")[1]
    busiPartyUuid=fileContent.split(",")[2]
    accesstoken=fileContent.split(",")[3]
    report_id=fileContent.split(",")[4]
    print("用户:" + partyName + "的线程已启动,启动时间为:",time.time())
    url = "http://inet-local-k8s-master.yuanbaopu.com:38207/rc/test/access/req"
    headers={"Content-Type":"application/json"}
    body_data="""
    {
    "merNum": "MER_1001",
    "orgNum": "ORG_20171228ZHMBUAVC",
    "proNum": "PRO_20171228ESWWNUCD",
    "data": {
        "loan": {
            "applyAmount": "500",
            "applyCityCode": "330100",
            "applyLimit": "",
            "applyTime": "2018-05-30 09:56:00",
            "timeUnit": "",
            "userFor": "备货"
        },
        "per": {
            "bankCard": "",
            "busiPartyUuid": "%s",
            "education": "",
            "fcName": "",
            "fcPhone": "",
            "frZipCode": "330100",
            "hsSituation": "",
            "hsType": "",
            "idCard": "%s",
            "isMarried": "2",
            "liveDetailAddr": "",
            "liveZipCode": "330100",
            "partyName": "%s",
            "phone": "15572826526",
            "scName": "",
            "scPhone": "",
            "hsAddress":"330100"
            },
        }
    }
    """ % (busiPartyUuid,idCard,partyName)
    req=urllib2.Request(url=url,headers=headers,data=bytes(body_data,"utf-8"))
    urllib2.urlopen(req)
    print("结束时间:",time.time())
    #response=codecs.decode(urllib2.urlopen(req).read(),"utf-8")

    #步骤二：将同盾接口返回值新增和修改到mysql
    #db=pymysql.Connection(user="dt",password="dtonly",db="data_transport",port=3306,charset="utf8",host="192.168.5.154")
    try:
        db = POOL.connection()
        cursor=db.cursor()
        #插入一条数据，为GET请求，用于获取datag返回的同盾贷前报告
        cursor.execute("""
        INSERT INTO http_data(request_host,request_url,request_method,request_body_parsed,request_body,response_body,mock_response_body,request_time,response_time,isMock,trueRequest,request_body_json,response_body_json,mock_response_body_json) VALUES ('192.168.5.51','/api/getNotify/%s','GET','/api/getNotify/%s','/api/getNotify/%s',NULL,'{"kind":"dq","kid":"%s","step":"DOWNLOAD_END","info":{"apply_time":1534495406000,"risk_items":[{"risk_level":"low","item_name":"3个月内身份证关联多个申请信息","item_id":1856897,"item_detail":{"frequency_detail_list":[{"detail":"3个月身份证关联家庭地址数：0"},{"detail":"3个月身份证关联手机号数：2","data":["15572828888","152※※※※0092"]}],"type":"frequency_detail"},"group":"客户行为检测"},{"risk_level":"low","item_name":"7天内设备或身份证或手机号申请次数过多","item_id":1856917,"item_detail":{"frequency_detail_list":[{"detail":"7天内手机号申请次数：10"}],"type":"frequency_detail"},"group":"客户行为检测"},{"risk_level":"medium","item_name":"1个月内申请人在多个平台申请借款","item_id":1856957,"item_detail":{"platform_detail_dimension":[{"dimension":"借款人手机详情","detail":["小额贷款公司:1"],"count":1},{"dimension":"借款人身份证详情","detail":["一般消费分期平台:1","小额贷款公司:1"],"count":2}],"platform_detail":["一般消费分期平台:1","小额贷款公司:1"],"type":"platform_detail","platform_count":2},"group":"多平台借贷申请检测"},{"risk_level":"medium","item_name":"3个月内申请人在多个平台申请借款","item_id":1856959,"item_detail":{"platform_detail_dimension":[{"dimension":"借款人手机详情","detail":["小额贷款公司:1"],"count":1},{"dimension":"借款人身份证详情","detail":["一般消费分期平台:1","小额贷款公司:1"],"count":2}],"platform_detail":["一般消费分期平台:1","小额贷款公司:1"],"type":"platform_detail","platform_count":2},"group":"多平台借贷申请检测"}],"address_detect":{"id_card_address":"北京市市辖区东城区","mobile_address":"湖北省仙桃市"},"final_decision":"Accept","report_time":1534495406000,"report_id":"%s","application_id":"1808171643268628CC2D342865C702C4","final_score":14,"success":true,"companyName":"","businessId":""},"accesstoken":"%s"}',NOW(),NOW(),1,0,NULL,NULL,NULL)
        """ % (accesstoken,accesstoken,accesstoken,partyName,report_id,accesstoken))
        db.commit()
        db.close()
        #对表中的request_body_parsed字段根据身份证号和姓名进行轮询，若存在则进行修改操作,为POST请求
        time_sum=0
        while(True):
            db = POOL.connection()
            time.sleep(5)
            sql = """
             SELECT * FROM http_data WHERE request_body_parsed LIKE 'fcName=&fcPhone=&sign=%%&time=%%&id_number=%s&kind=dq&kid=%s&appId=10020&mobile=15572826526'
            """ % (idCard, partyName)
            cursor.execute(sql)
            cursorResult = cursor.fetchall()
            time_sum=time_sum+5
            if len(cursorResult)!=0 and len(cursorResult[0])>4:
                if  cursorResult[0][0]>0:
                    idd=cursorResult[0][0] #获取id
                    try:
                        #db.begin()
                        cursor.execute("begin;")
                        cursor.execute("""
                        UPDATE http_data SET mock_response_body='{"msg":"成功","code":"10000","report_id":"%s","step":"LOGIN_END","accesstoken":"%s"}',isMock=1,trueRequest=0 WHERE id=%d;
                        """ % (report_id,accesstoken,idd))
                        #db.commit()
                        cursor.execute("commit;")
                        db.close()
                        break
                    except Exception as e:
                        #db.rollback()
                        cursor.execute("rollback;")
                        print(e,"数据库异常")
            db.close()
            if time_sum>600:
                 print("break")
                 break
        db = POOL.connection()
        if time_sum > 600:
            print("用户%s,轮询超时" % partyName)
        else:
            #步骤三：等待N秒，当response_time>=request_time+设置的等待时间时(也就是datag将回调返回给了数据集市),数据集市再去调用datag回调接口
            time.sleep(40)
            url2 = "http://192.168.5.154:4433/ods/public/notify"
            body_data2="""
            {"accesstoken":"%s","status":1}
            """ % accesstoken
            req2=urllib2.Request(url=url2, headers=headers, data=bytes(body_data2, "utf-8"))
            urllib2.urlopen(req2)
    except Exception as e:
        print(e,"异常")
    finally:
        db.close()

threads = []
for i in range(len(fileContentList)):
    threads.append(threading.Thread(target=tongdunThread,args=(i,)))

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print("all over %s" % time.ctime())

# loop=asyncio.get_event_loop()
# tasks=[tongdunThread(i) for i in range(5)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
