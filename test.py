# coding=utf-8
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

f = 'dianyiok@163.com'
pwd = '010203ok'
sender = 'dianyiok@163.com'
receivers = ['2352956568@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = f
message['To'] = '2352956568@qq.com'
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)


try:
    smtpObj = smtplib.SMTP('smtp.163.com', 25)
    smtpObj.login(f, pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
    import traceback
    traceback.print_exc()
