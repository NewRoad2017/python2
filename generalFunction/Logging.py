# -*- coding: utf-8 -*-
import time
import sys
sys.path.append('D:/Applications/Python2/generalFunction')
from generalFunction import PathHelper,ReHelper,FileHelper
sys.path.append('D:/Applications/Python2/dataFileHelper')
from dataFileHelper import TxtHelper
class Logging:
    def __init__(self,dataDir):
        strTime = time.strftime('%Y%m%d_%H_%M_%S',time.localtime(time.time()))
        self.filePath = PathHelper.CombinePathpurely(dataDir,'logging'+strTime+'.txt')
        self.txtFile = TxtHelper.txtWrite(self.filePath)
    def WriteTrace(self,dataInfo):
        dataInfo = dataInfo+'\n'
        self.txtFile.Write(dataInfo)
    def Close(self):
        self.txtFile.Close()

if __name__ == '__main__':
    filePath = r'C:\Users\chenlu\Desktop\logs'
    filePath = ReHelper.replacePath(filePath)
    log = Logging(filePath)
    log.WriteTrace(filePath+u'陈璐~')
    # log.WriteTrace(u'陈璐~')
    log.WriteTrace("hh~")
    log.Close()
    print 2