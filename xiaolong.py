# coding=utf-8
import sys
import urllib2
import urllib
import cookielib

reload(sys)
sys.setdefaultencoding('utf-8')

proxy_support = urllib2.ProxyHandler({'http': '218.18.232.29:8080'})
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(
    proxy_support, urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.25 Safari/537.36'
           }
data = {
    'content': '''<p>我又来了，闲的蛋疼。</p>''',
    'referenceCommentId': '',
    'referenceCommenter': ''
}
sys.setrecursionlimit(1000000000)
page = 1
while page < 30082:
    try:
        req = urllib2.Request(
            'http://www.zuoxiaolong.com/message.do', urllib.urlencode(data), headers)
        res = urllib2.urlopen(req)
        print('page:%s,res:%s' % (page, res.read()))
        page += 1
    except Exception, e:
        print(e)
        continue
