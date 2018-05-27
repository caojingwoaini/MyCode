#--*-- coding:utf-8 --*--

import socket
import time
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",7777))
s.listen(3)

def tcplink(sock,addr):
    print("Connection waiting for %s:%s" % addr)
    sock.send(b"welcome")
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8")=="exit":
            break
        sock.send(("hello %s" % data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print("Connection %s:%s is closed" % addr)

while True:
    print("waiting connection...")
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()










