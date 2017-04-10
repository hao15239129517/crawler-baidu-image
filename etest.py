# coding=utf-8
import traceback

a = 1
b = 0
try:
    c = a / b
except Exception, e:
    print(e)
    # 打印出更详细的异常信息 和console窗口打印出的一样
    traceback.print_exc()
    print(traceback.format_exc())
