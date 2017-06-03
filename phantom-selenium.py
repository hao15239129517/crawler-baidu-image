# coding=utf-8
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
reload(sys)
sys.setdefaultencoding('utf-8')
# 如果没有设置python环境变量 要把实际路径放进去executable_path="D:\Python27\Scripts\phantomjs.exe"
driver = webdriver.PhantomJS()
# 设置全屏
driver.maximize_window()
driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys(u'菜鸟')
driver.find_element_by_id('su').click()
# 要有一定的停顿 来等待网络响应
sleep(1)
driver.find_element_by_class_name('n').click()

driver.get(
    'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')
sleep(2)
driver.execute_script(
    'document.body.scrollTop=800;')
sleep(2)
driver.save_screenshot('douban-movie1.jpg')
driver.execute_script(
    'document.body.scrollTop=1800;')
sleep(10)
driver.save_screenshot('douban-movie2.jpg')
driver.quit()
print('ok')
