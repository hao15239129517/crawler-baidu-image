# coding=utf-8
import time
import urllib
import LogHelper

from apscheduler.schedulers.blocking import BlockingScheduler
# 一般就用这个
scheduler = BlockingScheduler()
'''
参数信息   地址：http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html#module-apscheduler.triggers.cron
Parameters:    
year (int|str) – 4-digit year
month (int|str) – month (1-12)
day (int|str) – day of the (1-31)
week (int|str) – ISO week (1-53)
day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
hour (int|str) – hour (0-23)
minute (int|str) – minute (0-59)
second (int|str) – second (0-59)
start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
'''
'''
表达式表达的意思
Expression    Field    Description
*    any    Fire on every value
*/a    any    Fire every a values, starting from the minimum
a-b    any    Fire on any value within the a-b range (a must be smaller than b)
a-b/c    any    Fire every c values within the a-b range
xth y    day    Fire on the x -th occurrence of weekday y within the month
last x    day    Fire on the last occurrence of weekday x within the month
last    day    Fire on the last day within the month
x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
'''


def my_job():
    time.sleep(10)
    print 'hello world'
    print(scheduler.running)
scheduler.add_job(my_job, 'cron', minute=19)
print(scheduler.running)
while True:
    print(scheduler.running)
    if not scheduler.running:
        scheduler.start()
