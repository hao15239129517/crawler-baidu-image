# coding=utf-8
import sys
from PIL import Image
reload(sys)
sys.setdefaultencoding('utf-8')
# 1、安装pillow   2、安装pytesseract  3、安装tesseract-ocr-setup-4.00.00dev.exe 文件
# 并且要加到path里面

import pytesseract
print(pytesseract.image_to_string(
    Image.open(r'ValidateCode.jpg')))
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
