#coding=utf-8
import urllib2
import re
import HTMLParser

def getHtml(url1):
    f = file('titles.txt', 'a')
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    for i in range(1, 201):
        url = url1 + str(i)
        request = urllib2.Request(url, headers=headers)
        page = urllib2.urlopen(request)
        html = page.read().decode('utf-8')
        rec = re.compile(r'<a class="titlelnk" href=".*?" target="_blank">(.*?)</a>')
        list = re.findall(rec, html)
        html_parser = HTMLParser.HTMLParser()
        f.write('------------------------------第'+str(i)+'页--------------------------------------\n')
        #必须要分开加u
        print '------------------------------'+u'第'+str(i)+u'页'+'--------------------------------------'
        for l in list:
            f.write(html_parser.unescape(l).encode('utf-8') + '\n')
            f.flush()
    f.close()
    return 'ok'
print getHtml('http://www.cnblogs.com/sitehome/p/')
