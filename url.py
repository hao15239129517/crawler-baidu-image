# coding=utf-8
import urllib

def test():
    print urllib.urlencode({"offset": 10, "start": "0"})
test()