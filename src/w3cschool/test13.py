# coding=utf-8
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

maillist = ['test@cn.ibm.com']
mail_host = 'smtp.163.com'
mail_user = 'test@163.com'
mail_pass = '********'
mail_postfix="163.com"

def sendMail(to,subject,message):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(message,_subtype='plain',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = subject    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to)
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception as e:  
        print(str(e))
        return False

if __name__ == '__main__' :
    if sendMail(maillist,"Mail test","Mail test."):
        print("发送成功")
    else:
        print("发送失败")