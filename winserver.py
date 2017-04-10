# coding=utf-8
import sys
import logging
from logging.handlers import RotatingFileHandler
import datetime
import os
import win32serviceutil
import win32service
import win32event
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    # 必须要指定 sys.path[0] 得到的是这个文件所在的路径  如果不指定就跑到win32所在的路径下了
    logPath = os.path.join(sys.path[0], 'log')

    if not os.path.exists(logPath):
        os.makedirs(logPath)
    handler = RotatingFileHandler(
        os.path.join(logPath, '%s.txt' % datetime.date.today()), maxBytes=5 * 1024 * 1024, backupCount=10)
    handler.setLevel(level=logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.error('error')


class PythonService(win32serviceutil.ServiceFramework):

    # 服务名
    _svc_name_ = "WinServiceTest"
    # 服务显示名称
    _svc_display_name_ = "WinServiceTest"
    # 服务描述
    _svc_description_ = "WinServiceTest description"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        while True:  # 要加while循环 否则服务只能运行1次 启动服务时有提示
            log()
            time.sleep(20)

    def SvcStop(self):
        # 先告诉SCM停止这个过程
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # 设置事件
        win32event.SetEvent(self.hWaitStop)
# 必须要加 否则会出现Python could not import the service's module 错误代码1
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)
