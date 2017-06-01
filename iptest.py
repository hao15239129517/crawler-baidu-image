# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import urllib2
import urllib
import time
import socket
import random
# 特稳定IP 107.151.152.218:80
# http://www.xicidaili.com/wn/测试可用IP '107.151.136.202:80',222.124.130.34:8080,'103.14.196.74:8080','107.151.142.114:80''54.169.238.128:9999'
#agent = ['49.113.101.167:8090','113.78.28.205:8090','219.136.31.16:8090','119.131.83.227:8090','221.221.206.208:8090','116.52.16.57:8090','182.109.80.149:9000','59.55.59.41:9000','115.223.201.206:9000']
proxy_support = urllib2.ProxyHandler({'http': '218.18.232.29:8080'})

opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
try:
    response = urllib2.urlopen('http://zhao.zhixinst.com/Default.aspx')

    print(response.read())
except Exception, e:
    print e

print('*' * 50)
exit(0)
import urllib2
import socks
from sockshandler import SocksiPyHandler

opener = urllib2.build_opener(
    SocksiPyHandler(socks.SOCKS5, "116.226.90.12", 808))
print urllib2.urlopen("http://zhao.zhixinst.com/Default.aspx").read()
