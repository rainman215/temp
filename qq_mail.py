#! /usr/bin/env python
#coding=GB18030
# from email import MIMEMultipart
from email.mime.multipart import MIMEMultipart 
from email.MIMEBase import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib



mailto_list = ['long.cheng@keliangtek.com']           # �ռ���(�б�)
mail_host = "smtp.exmail.qq.com:465"            # ʹ�õ������smtp��������ַ��������qq��smtp��ַ
mail_user = "long.cheng@keliangtek.com"                           # �û���
mail_pass = "GDhSYRc5f84NTYsC"                             # ����
mail_postfix = "keliangtek.com"  # ����ĺ�׺


def send_mail(to_list, sub, content):
    me = mail_user+"@"+mail_postfix
    new_report = [r"E:\name.txt", "name.txt"]
    print(new_report[0])
    msg = MIMEMultipart()
    msg['Subject'] = sub                    # ����
    msg['From'] = me
    msg['To'] = ";".join(to_list)                # ���ռ����б��ԡ������ָ�
    # �ı�����
    text_content = MIMEText(content)
    msg.attach(text_content)
    # ����
    attachment = MIMEApplication(open(new_report[0], 'rb').read())
    attachment.add_header("Content-Disposition", "attachment", filename=new_report[1])
    msg.attach(attachment)
    try:
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
        server.login(mail_user, mail_pass)               
        server.sendmail(me, to_list, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(str(e))
        return False
for i in range(1):                             # ����1�⣬������б��Ǽ����ˣ�������
    if send_mail(mailto_list, u"���Ա���", 'test'):  # �ʼ�������ʼ�����
        print("done!")
    else:
        print("failed!")

