# coding=utf-8
import urllib2
import traceback

# 西刺代理 http://www.xicidaili.com/nn/
# 检查代理http://ip.chinaz.com/getip.aspx
proxy_support = urllib2.ProxyHandler({'http': '220.166.96.90:82'})
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3107.4 Safari/537.36'
}
opener = urllib2.build_opener(proxy_support)
try:
    request = urllib2.Request(
        'http://ip.chinaz.com/getip.aspx', headers=headers)
    response = opener.open(request)
    print(response.read())
except:
    print traceback.format_exc()

print('*' * 50)
