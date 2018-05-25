#--*-- coding:utf-8 --*--

import socket
import threading
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建一个服务端的socket
s.bind(("127.0.0.1",7777))  #服务端socket将socket绑定到地址，也就是指定用于客户端连接的ip和端口
s.listen(3)  #等待连接的最大数量为3
print("waiting for connection...")

def tcplink(sock,addr):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b"Welcome")  #服务端socket发送数据，这里所发送的数据必须是bytes字节
    while True:
        data=sock.recv(1024)  #服务端socket能够接收的最大数据量
        time.sleep(1)  #每隔一秒钟轮询一次,看有没有客户端socket发送数据
        if not data or data.decode("utf-8")=="exit":  #将客户端没有发送数据或者发送数据为"exit"
            break
        sock.send("hello,%s!" % data.decode("utf-8")).encode("utf-8")  #服务端socket接收到客户端socket所发送的数据之后，发送给客户端socket的数据
    sock.close()
    print("Connection from %s:%s closed" % addr)




while True:
    sock,addr=s.accept() #接受tcp并返回新服务端的socket，这个socket可以用来接收客户端的数据和发送数据到客户端；返回新的socket和新的地址（这个地址包含ip和端口）
    t=threading.Thread(target=tcplink,args=(sock,addr))  #创建一个线程，target为该线程需要执行的函数，args为所执行函数需要的参数
    t.start()  #启动该线程






