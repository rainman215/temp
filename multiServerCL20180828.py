#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Event
import os
import threading
import time

import socketserver


event = threading.Event()

sock=[]
# flag=0
_e=Event()
_s=Event()
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        address,port=self.client_address
        sock.append(self.request)
        print type(str(self.client_address))
        try:
            while True:
                self.data=self.request.recv(1024)
#                 print("{} send:".format(self.client_address),self.data)
                if not self.data:
                    print("connection lost")
                    break
                for re in sock:
                    data=self.data.decode('utf-8')
                    with open('file.txt','w') as f:
                        f.write(data)
                    data=address+' send:'+data
                    re.sendall(data.encode('utf-8'))
                    _e.set()
#                 self.request.sendall(self.data.upper())
        except Exception as e:
            print(self.client_address,"连接断开")
        finally:
            self.request.close()
    def setup(self):
        print("before handle,连接建立：",self.client_address)
    def finish(self):
        print("finish run  after handle")

def _event():
    while True:
#         print event.isSet()
        _e.wait()
        with open('file.txt','r') as f:
            line=f.readlines()
            if 'run' in line:
                print "run111"
                run=threading.Thread(target=start)
                run.setName('run')
                run.start()
            if 'pause' in line:
                print "run222"
                run2=threading.Thread(target=pause)
                run2.setName('pause')
                run2.start()
            if 'stop' in line:
                print "run333"
                run3=threading.Thread(target=stop)
                run3.setName('stop')
                run3.start()
#                 print event.isSet()
        _e.clear()
#                 os.remove('file.txt')
def start():
    while True:
        for i in threading.enumerate():
            if 'pause' in str(i):
                print 'pause'
                print threading.enumerate()
                _s.wait()
            if 'stop' in str(i):
                print 'stop'
                raise Exception("执行退出")   
#                 _s.wait()
                
        print "start"
#         time.sleep(2)
#     t1=threading.Thread(target=main)
def pause():
    print "pause"
    _s.clear()
    
def stop():
    print "stop"
    _s.set()
    
def main():
    HOST,PORT = "172.20.4.50",12345
    server=socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
    
threads=[]
t1=threading.Thread(target=main)
threads.append(t1)
t2=threading.Thread(target=_event)
threads.append(t2)
for t in threads:
    t.setDaemon(True)
    t.start()
for i in threads:
    i.join()
    

# if __name__=="__main__":
#     HOST,PORT = "172.20.4.50",12345
#     server=socketserver.TCPServer((HOST,PORT),MyTCPHandler)
#     server.serve_forever()