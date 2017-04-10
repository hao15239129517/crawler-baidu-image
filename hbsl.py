# coding=utf-8
# from 和直接 import导包的区别是 from  更具体使用函数的时候就不用加包名了 而使用 import方式
# 在调用函数的时候还要加上包名.的形式调用
import urllib
import bs4
import re
import sqlalchemy
from sqlalchemy.sql import select
import sys
import time
sys.setrecursionlimit(1000000000)
reload(sys)
sys.setdefaultencoding('utf-8')
params = urllib.quote_plus(
    "DRIVER={SQL Server Native Client 10.0};SERVER=.;DATABASE=test;UID=sa;PWD=AbCd1234")
engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
conn = engine.connect()
metaData = sqlalchemy.MetaData(bind=engine)
newsTable = sqlalchemy.Table('news', metaData, autoload=True)
page = 1
while page < 382:
    if page != 1:
        url = 'http://www5.ncwu.edu.cn/channels/4_%s.html' % page
    else:
        url = 'http://www5.ncwu.edu.cn/channels/4.html'
    html = urllib.urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    if soup == None:
        continue
    div = soup.find('div', class_='xinxilist')
    ul = div.find('ul')
    for li in ul.find_all('li'):
        href = li.find('a')['href']
        date = li.find('i').get_text()
        id = re.search(r'(\d+).html', href).groups(1)[0]
        title = li.find('a').get_text()
        try:
            # 发生  网络异常
            time.sleep(1)
            html = urllib.urlopen(href)
            contentHtml = bs4.BeautifulSoup(html.read(), 'html.parser')
        except Exception, e:
            print(e)
            continue

        if contentHtml == None:
            continue
        content = contentHtml.find('div', attrs={'align': 'left'})
        if content == None:
            continue
        content = content.find_parent('div', attrs={'align': 'center'})
        if content == None:
            continue

        res = conn.execute(select([newsTable]).where(newsTable.c.id == id))
        if res.fetchone() == None:
            conn.execute(newsTable.insert().values(
                id=id.strip(), href=href.strip(), title=title.strip(), date=date.strip(), content=content.prettify()))
        else:
            continue
    print('page：%s' % page)
    page += 1
print('---------------------------ok------------------------------------')
