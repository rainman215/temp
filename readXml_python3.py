#! /usr/bin/env python
#coding=utf-8

import xml.dom.minidom as xmldom

class readXml(object):
    def __init__(self,strxml):
        self.xml_file=xmldom.parse(strxml)
        self.eles=self.xml_file.documentElement
    #获取标签对之间文本
    def getTabValue(self,item,i):        
        tagName=self.eles.tagName
        tabValue=self.eles.getElementsByTagName(item)[i].firstChild.data 
        print(tabValue)
        return tabValue
    #获取标签属性值
    def item_getAttribute(self,item,i,text):
        itemlist=self.eles.getElementsByTagName(item)
#         print(itemlist)
        attribute=itemlist[i].getAttribute(text)
        print(attribute)
        return attribute
        
    
if __name__ =='__main__':
    strxml=r'C:\Users\KLJS154\QuiKLab3\config.xml'
    item='item'
    text='run'
    d=readXml(strxml)
#     d.getTabValue(item,0)
    d.item_getAttribute(item,2,text)
    