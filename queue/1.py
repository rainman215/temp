#! /usr/bin/env python
#coding=GB18030
import queue

q=queue.Queue(5)    #��������ó���,Ĭ��Ϊ���޳�
print(q.maxsize)    #ע��û������
q.put(123)
q.put(456)
q.put(789)
q.put(100)
q.put(111)
# q.put(233)
print(q.get())
print(q.get())
print(q.get())