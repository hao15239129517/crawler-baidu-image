# coding=utf-8
import sys
import logging
from logging.handlers import RotatingFileHandler
import datetime
import os

reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logPath = 'log'

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
logger.info('info')
logger.warning('warning')