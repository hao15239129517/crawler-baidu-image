import urllib
import re
import string


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    start = string.index(html, '<div class="content">')
    end = string.index(html, '<div class="pagebreak">')
    rec=re.compile(r'(\d+.\d+.\d+.\d+.:\d+)@')
    list=re.findall(rec,html[start:end])
    f=file('d:\ips.txt','a')
    for l in list:
        f.write(l+'\n')
    f.close()
    return list
print getHtml('http://www.youdaili.net/Daili/guonei/10708.html')
