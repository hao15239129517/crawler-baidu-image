# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

f = 'dianyiok@163.com'
pwd = '010203ok'
t = '2352956568@qq.com'

message = MIMEMultipart()

message['From'] = f
message['To'] = t
message['Subject'] = '我是主题'
message.attach(MIMEText('我是邮件内容', 'plain', 'utf-8'))
# 构造附件
# att1 = MIMEText(open('titles.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="titles.txt"'
# message.attach(att1)

server = smtplib.SMTP('smtp.163.com', 25)
server.set_debuglevel(1)
server.login(f, pwd)
server.sendmail(f, t, message.as_string())
server.quit()
print('ok')
