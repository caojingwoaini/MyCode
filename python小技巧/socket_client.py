#--*-- coding:utf-8 --*--

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建一个客户端socket
s.connect(("127.0.0.1",7777))  #客户端socket与服务端socket建立连接
print(s.recv(1024).decode("utf-8"))  #客户端socket接收服务端所发送的欢迎消息
for data in [b"gaokun",b"fanyanwei",b"xuzhen"]:
    s.send(data)  #客户端socket发送数据
    print(s.recv(1024).decode("utf-8"))  #客户端socket接收到服务端socket所发送的数据
s.send(b"exit")
s.close()  #关闭客户端socket








