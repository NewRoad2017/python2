# -*- encoding: utf8 -*-
import win32com
from win32com.client import Dispatch
import win32com.client
import sys
import re
import string

reload(sys)
sys.setdefaultencoding('utf8')


# from fileinput import filename

class Word(object):
    # 初始化word对象
    def __init__(self, uri):
        self.objectword(uri)

    # 创建word对象
    def objectword(self, url):
        self.word = win32com.client.Dispatch('Word.Application')
        self.word.Visible = 0
        self.word.DisplayAlerts = 0

        self.docx = self.word.Documents.Open(url)
        self.wrange = self.docx.Range(0, 0)

    # 关闭word
    def close(self):
        self.word.Documents.Close()
        self.word.Quit()

    # 创建word
    def create(self):

        pass

    # 在word中进行查找
    def findword(self, key):
        question = []
        uri = r'E:\XE\ctb.docx'
        self.objectword(uri)
        # 读取所有的word文档内容
        range = self.docx.Range(self.docx.Content.Start, self.docx.Content.End)
        question = str(range).split("&")
        # 查找内容
        # question = re.split(r"(\r[1][0-9][0-9]+.)",str(range))
        # l = question[0].split("\d+.")
        for questionLine in question:
            questionLine = questionLine.strip('\n')
            l = re.split(r"([1][0-9][0-9]+.)", questionLine)
            del l[0]
            for t in l:
                s = str(key[0:3])
                if str(t).find(s) > -1:
                    # 插入
                    g = string.join(l)

                    print g.encode('gb2312')
                    # print g.decode("")
                    self.insertword(g)
                    print "sss"
                else:
                    print "ttt"

    # 插入word
    def insertword(self, w):
        url = r'E:\XE\ctb.doc'
        self.objectword(url)
        self.wrange.InsertAfter(w)
        pass

    # 读取数据源
    def source(self, src):
        f = open(src)
        d = f.readlines()
        for l in d:
            name, question01, question02, question03, question04, question05 = tuple(l.decode('utf8').split('\t'))
            if question01 != u'全对':
                # self.wrange.InsertAfter(name)
                self.findword(question01)
        return self

filePath = r'C:\Users\chenlu\Desktop\word Version\words\south_15\陈璐.doc'
#filePath = ReHelper.replacePath(filePath)
Word(filePath).close()