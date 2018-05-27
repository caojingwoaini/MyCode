#-*- coding:utf-8 -*-


#可以理解为消费者
def consumer():
    r="consumer is start"  #这里所为了消费者第一次启动时，所打印的信息
    while True:
        n=yield r
        if not n:
            return
        print("[CONSUMER] Consuming %s..." % n)
        r="200 ok"

#可以理解为生产者
def produce(c):
    print(c.send(None))  #生成器的send方法，第一次调用时，只能传"None"；之后能够传为空的字符串，例如"";这里会返回consumer函数里的r变量(第一次的r变量)
    n=0
    while n<5:
        n=n+1
        print("[PRODUCER Producing %s...]" % n)
        r=c.send(n)  #调用消费者的函数所返回的值,这里会返回consumer函数里的n变量；也就是最终会返回consumer函数的r变量（第二次的r变量）
        print("[PRODUCER] Consumer return: %s" % r)
    c.close()

j1=consumer()
produce(j1)

"""
返回结果如下：
consumer is start
[PRODUCER Producing 1...]
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 ok
[PRODUCER Producing 2...]
[CONSUMER] Consuming 2...
[PRODUCER] Consumer return: 200 ok
[PRODUCER Producing 3...]
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 ok
[PRODUCER Producing 4...]
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 ok
[PRODUCER Producing 5...]
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 ok
"""


















