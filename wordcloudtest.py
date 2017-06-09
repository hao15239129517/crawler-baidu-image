# coding=utf-8
import sys
import jieba
import codecs
from wordcloud import WordCloud
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf-8')

# 输出图片显示窗口
# 中文显示 要是用本地中文字体 否则显示乱码


def get():

    with codecs.open('wordcloud.txt',  encoding='gbk') as f:
        txt = f.read()
    txt = ' '.join(jieba.cut(txt))
    word = WordCloud(font_path='msyhl.ttc').generate(txt)
    plt.figure()
    plt.imshow(word)
    plt.axis('off')
    plt.show()

# 保存成图片


def getJpg():
    with codecs.open('wordcloud.txt',  encoding='gbk') as f:
        txt = f.read()
    txt = ' '.join(jieba.cut(txt))
    word = WordCloud(
        font_path='msyh.ttc', background_color='#ccc', width=800, height=800).generate(txt)
    word.to_file('ss.jpg')

if __name__ == '__main__':
    getJpg()
