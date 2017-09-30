# -*- coding: utf-8 -*-
from win32com import client
import os
import sys
sys.path.append('D:/Applications/Python2/generalFunction')
from generalFunction import PathHelper,ReHelper,FileHelper,Logging

class Word:
    def __init__(self, dataPath):
        self.filePath = dataPath
        self.word = client.Dispatch('Word.Application')
        self.word.Visible = 0
        self.word.DisplayAlerts = 0
        self.wordDocu = self.word.Documents.Open(self.filePath)

    def SavaAsDocx(self):
        pathParts = os.path.split(self.filePath)
        filename = pathParts[1]
        filenameOnly = os.path.splitext(filename)[0]
        tarPath =pathParts[0]+ "\\" + filenameOnly +'.docx'#r'\'是不可以的
        self.wordDocu.SaveAs(tarPath, 16)  # 17对应于下表中的pdf文件

    def Close(self):
        self.wordDocu.Close()

    def Quit(self):
        self.word.Quit()


if __name__ == "__main__":
    str = [ u'\u60a8\u8bd5\u56fe\u6253\u5f00\u7684\u6587\u4ef6\u7c7b\u578b\u88ab\u4fe1\u4efb\u4e2d\u5fc3\u7684\u6587\u4ef6\u963b\u6b62\u8bbe\u7f6e\u963b\u6b62\u3002']
    print str[0]
    # fileDir = r'C:\Users\chenlu\Desktop\word Version\words\south_15'
    # fileDir = ReHelper.replaceDir2(fileDir)
    # filePath = fileDir+u'陈璐.doc'
    # filePath = u'C:\\Users\\chenlu\\Desktop\\word Version\\words\\south_15\\陈璐.doc'
    # filePath.decode('utf-8')
    word = Word(filePath)
    word.SavaAsDocx()
    word.Close()
    print (2)