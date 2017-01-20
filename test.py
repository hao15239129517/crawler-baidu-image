#coding=utf-8
import urllib
import os

key='高圆圆'
path=unicode(r'D:\bdimg\%s'%key,'utf-8')
if not os.path.exists(path):
    os.mkdir(path)
print(urllib.quote('微距摄影'))