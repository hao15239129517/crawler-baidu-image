# coding=utf-8
import sys
import os
import ConfigParser

print(sys.path[0])
reload(sys)
sys.setdefaultencoding('utf-8')

config = ConfigParser.ConfigParser()
config.read(os.path.join(sys.path[0], 'config.ini'))
print(config.get('section', 'html'))
