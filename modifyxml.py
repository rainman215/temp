#! /usr/bin/env python
#coding=utf-8
import xml.etree.cElementTree as ET
# from lxml import etree
# from tqdm import tqdm
import os
class xmlReader(object):
    def __init__(self,path):
        self.path=path
        self.tree=ET.ElementTree(file=self.path)
        self.root=self.tree.getroot()
    def getNodeText(self,xpath):
        self.root=self.tree.getroot()
        node=self.root.find(xpath)
        return(node.text)
    def modifyNodeText(self,xpath,value):
        node=self.root.find(xpath)
        node.text=value
        self.tree.write(self.path,encoding='utf-8')
    def modifyAttrValue(self,tag,attr,value,num=0):
        i=0
        for n in self.root.iter(tag):
            if i==num:
                print("11111")
                n.set(attr,value)
            i=i+1
            print(n.attrib)
        self.tree.write(self.path,encoding='utf-8')
if __name__=='__main__':
    path=r'C:\Users\KLJS154\QuiKLab3\config.xml'
    
    op=xmlReader(path)
    xpath='item'
    # print(op.getNodeText(xpath))
    # op.modifyNodeText(xpath,'5')
    op.modifyAttrValue(xpath, 'name', 'no1')
    # tree.write(path,encoding='utf-8')