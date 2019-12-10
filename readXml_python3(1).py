#! /usr/bin/env python
#coding=utf-8

import xml.dom.minidom as xmldom
import xml.etree.ElementTree as ET
import os
class readXml(object):
    def __init__(self,strxml):
        self.xml_file=xmldom.parse(strxml)
        self.eles=self.xml_file.documentElement
        self.updateTree=ET.parse(strxml)
        self.root=self.updateTree.getroot()
    #获取标签对之间文本
    def getTabValue(self,item,i):        
        tagName=self.eles.tagName
        tabValue=self.eles.getElementsByTagName(item)[i].firstChild.data         
        print(tabValue)
        return tabValue
    #获取标签属性值
    def item_getAttribute(self,item_a,i,text):
        itemlist=self.eles.getElementsByTagName(item_a)
        attribute=itemlist[i].getAttribute(text)
        print(attribute)
        
        return attribute
   #修改XML标签对之间文本
    def setAlltabValue(self,tab_name,lab_text): 
        for i in self.root.iter(tab_name):
            print(i.tag,i.attrib,i.text)
            for j in i.iter(tab_name):
                print('修改之前的文本……',j.text)
                j.text=lab_text
                print('修改之后的文本……',j.text)
        self.updateTree.write(strxml)  
             
    #修改XML属性值   
    def setAllattrib(self,lab_attribname,t,name,lab_attribtext):
        datas=[]
        for i in self.root.iter(lab_attribname):
            mydict=i.attrib
            datas.append(mydict)
        print(datas)
        print('修改之前……',datas[t])
        if name in datas[t]:
            datas[t][name]=lab_attribtext
        print('修改之后……',datas[t])
#                 print('name')
            #修改属性值
#             for j in i.iter(lab_attribname):
#                 print('修改之前的属性值',j.attrib)
#                 j.attrib[name]=lab_attribtext
#                 print('修改之后的属性值:',j.attrib)
        self.updateTree.write(strxml,encoding='utf-8')
     
    #增加标签
    def add_tag(self,newEle_name,newEle_attrib,newEle_text):
        newEle=ET.Element(newEle_name)
        newEle.attrib=newEle_attrib
        newEle.text=newEle_text
        self.root.append(newEle)
        self.updateTree.write(strxml,encoding='utf-8')
        
if __name__ =='__main__':
    strxml=r'C:\Users\KLJS154\QuiKLab3\config.xml'
#     updateTree=ET.parse(strxml)
#     root=updateTree.getroot()
    item_a='item'
    tab_name='port'
    text='name2'
    lab_text='woen'
    lab_attribname='item'
    lab_attribtext='7'
    name=u'run'
    newEle_name=u'newElement'
    newEle_attrib={'name':'newElement','age':'20'}
    newEle_text='This is a new elemnet'
    d=readXml(strxml)
    t=0
#     d.getTabValue(item,0)
#     d.item_getAttribute(item_a,1,text)
#     d.setAlltabValue(tab_name, lab_text)
    d.setAllattrib(lab_attribname,t, name,lab_attribtext)
#     d.add_tag(newEle_name, newEle_attrib, newEle_text)





    