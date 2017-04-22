# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 1、安装pillow   2、安装pytesseract  3、安装tesseract-ocr-setup-4.00.00dev.exe 文件
# 并且要加到path里面
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open(r'E:\Image.do')))
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
