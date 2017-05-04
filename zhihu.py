# coding=utf-8
import sys
import urllib
import urllib2
import cookielib
import time

reload(sys)
sys.setdefaultencoding('utf-8')

# 创建一个cookie实例
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.25 Safari/537.36'
           }

picture = opener.open(
    'https://www.zhihu.com/captcha.gif?r=%s&type=login' % int(round(time.time() * 1000))).read()
local = open('captcha.gif', 'wb')
local.write(picture)
local.close()

captcha = raw_input('请输入验证码：')

data = {'_xsrf': '911a5fd89b7dde56acd38d5b046550f1',
        'password': 'xx',
        'captcha': captcha,
        'phone_num': '18721106149'
        }
req = urllib2.Request(
    'https://www.zhihu.com/login/phone_num', urllib.urlencode(data), headers)
res = opener.open(req)
print(res.read().decode('unicode-escape').encode('utf-8'))
for c in cookie:
    print('%s--%s' % (c.name, c.expires))
    c.expires = 1995962843
for c in cookie:
    print('%s--%s' % (c.name, c.expires))

req = urllib2.Request('https://www.zhihu.com/', headers=headers)
res = opener.open(req)
print(res.read())
