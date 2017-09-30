# -*- coding: utf-8 -*-
import sys
sys.path.append("D:/Applications/Python3/generalFunction")
from generalFunction import ReHelper,PathHelper
import time

class TXT:
    def __init__(self,dataPath):
        self.filePath = dataPath
    def Close(self):
        pass


class txtRead(TXT):
    def __init__(self,dataPath):
        TXT.__init__(self,dataPath)
        self.fileRead = open(self.filePath,'r')
    def ReadLines(self):
        self.listRows = self.fileRead.readlines()
    def Read(self):
        strContent = self.fileRead.read()
        self.listRows = strContent.split('\n')
    def Close(self):
        self.fileRead.close()

class txtWrite(TXT):
    def __init__(self,dataPath):
        TXT.__init__(self,dataPath)
        self.fileWrite = open(self.filePath,'w')
    def Write(self,dataString):
        self.fileWrite.write(dataString)
    def Close(self):
        self.fileWrite.close()


if __name__ == '__main__':
    # filePath = r'C:\Users\chenlu\Desktop\tests\test0921.txt'
    # txt = txtRead(filePath)
    # txt.ReadLines()
    # l = txt.listRows
    # y = txt.listRows[0].decode('utf-8')
    # list = [y]
    filePath = r'C:\Users\chenlu\Desktop\tests\test0921_2.txt'
    txt = txtWrite(filePath)
    x = '陈璐'.decode('utf-8').encode('GB2312')
        # .encode('utf-8')
    y = u'陈璐陈璐'
    y = y.encode('utf-8')
    txt.Write(x)
    # txt.Write(y)
    txt.Close()


    strTime = time.strftime('%Y%m%d_%H_%M_%S', time.localtime(time.time()))
    fileDir = r'C:\Users\chenlu\Desktop\logs'
    filePath = PathHelper.CombinePathpurely(fileDir, 'log'+strTime+'.txt')
    #filePath = r'C:\Users\chenlu\Desktop\word Version\south_33_register\test.txt'
    filePath = ReHelper.replacePath(filePath)
    txt = txtWrite(filePath)
    txt.Write("ss\n")
    txt.Write(u"陈")
    # data = txtread.fileRead.read()
    txt.Close()
    #print (txtread.listRows)


