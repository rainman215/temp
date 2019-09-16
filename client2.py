#!/usr/bin/env python
#coding:utf-8
import os
import socket
import threading
import time


# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('172.20.4.50', 12345))
def read_from_server(s):
    while True:
        data=s.recv(2048).decode('utf-8')
        if data:
            print('\n')
            print("Get MSG from server:",data)
            if 'run' in data:
                print("11111")
def send_message(s):
    while True:
        line = input('Please input something:')
        if line is None or line == 'exit':
            os._exit(0)
        # 将用户的键盘输入内容写入socket
        s.send(line.encode('utf-8'))
# 客户端启动线程不断地读取来自服务器的数据
threads=[]
t1=threading.Thread(target=read_from_server, args=(s, ))   # ①
threads.append(t1)
t2=threading.Thread(target=send_message,args=(s,))
threads.append(t2)
for t in threads:
    t.setDaemon(True)
#     print t.isAlive()
    t.start()
for i in threads:
    i.join()

