# coding=utf-8
import urllib
import json
from string import maketrans
import os
import socket
socket.setdefaulttimeout(10)
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}
intab = "wkv1ju2it3hs4g5rq6fp7eo8dn9cm0bla"
outtab = "abcdefghijklmnopqrstuvw1234567890"
trantab = maketrans(intab, outtab)

def deCode(url):
    # 先替换字符串
    for key, value in str_table.items():
        url = url.replace(key, value)
    # 再替换剩下的字符
    d = url.translate(trantab)
    return d

keywords="长腿美女"
path=unicode(r'D:\bdimg\%s'%keywords,'utf-8')
print(path)
if not os.path.exists(path):
    os.makedirs(path)
i=30
while i<=1000:
    url='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=%s&rn=30&gsm=1000000001e&1484808640351= HTTP/1.1'%(urllib.quote(keywords),urllib.quote(keywords),i)
    print(url)
    try:
        html = urllib.urlopen(url).read()
    except:
        continue
    jsons = json.loads(html)
    
    for item in jsons['data']:
        if 'objURL' not in item.keys():
            continue
        img = deCode(item['objURL'].encode('utf-8'))
        print(img)
        temp = img.split('/')
        imgname = temp[len(temp) - 1].replace('*', '#')
        if imgname.find('?') != -1:
            imgname = imgname[0:imgname.find('?')]
        if imgname.find('.') == -1:
            imgname = '%s.jpg' % imgname
        try:
            urllib.urlretrieve(img, os.path.join(path,imgname))
        except:
            continue
    i+=30
    print('ok')
print('all ok')    
# print(jsons['data'][0]['objURL'])
# print(type(jsons['data'][0]['objURL']))
# print(deCode('ippr_z2C$qAzdH3FAzdH3Frtv_z&e3Bcbrtv_z&e3Bv54AzdH3FcbrtvAzdH3F8cAzdH3FnlAzdH3Fa8AzdH3F991cbPIC0lK_8ad9_z&e3B3r2'))
# print(deCode(jsons['data'][0]['objURL'].encode('utf-8')))

