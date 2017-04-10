# coding=utf-8
import sys
import logging
from logging.handlers import RotatingFileHandler
import datetime
import os

reload(sys)
sys.setdefaultencoding('utf-8')


class LogHelper():

    @staticmethod
    def Log(msg, iserror=True):
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
        logPath = os.path.join(os.path.dirname(os.getcwd()), 'log')

        if not os.path.exists(logPath):
            os.makedirs(logPath)
        if iserror:
            logPath = os.path.join(logPath, '%s.txt' % datetime.date.today())
        else:
            logPath = os.path.join(
                logPath, '%s_info.txt' % datetime.date.today())
        handler = RotatingFileHandler(
            logPath, maxBytes=5 * 1024 * 1024, backupCount=10)
        handler.setLevel(level=logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(message)s ')

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info(msg)
        print(msg)
