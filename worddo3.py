# -*- coding: utf-8 -*-
from win32com import client
import sys
sys.path.append('D:/Applications/Python2/generalFunction')
from generalFunction import PathHelper,ReHelper,FileHelper,Logging
sys.path.append('D:/Applications/Python2/dataFileHelper')
from dataFileHelper import WordHelper
#from shutil import copy
import os

def SaveasDocxBatch(dataPathDir):
    print 'the Dir: %s' % (dataPathDir)
    listFiles = FileHelper.GetDirfiles(dataPathDir)
    for filename in listFiles:
        filePath = dataPathDir + filename
        nameOnly,extension = PathHelper.SplitfileName(filename)
        if extension == ".doc":
            print '%s extension:.doc' % filename
            word = WordHelper.Word(filePath)
            word.SavaAsDocx()
            print '%s convert to extension:.docx' % filename
            word.Close()
            os.remove(filePath)




#create log
# logPath = r'C:\Users\chenlu\Desktop\logs'
# logPath = ReHelper.replacePath(logPath)
# log = Logging.Logging(logPath)
#3. .doc Save as .docx
## win32com:the fileDir must to be split by '\\'

fileDir = r'C:\Users\chenlu\Desktop\word Version\words\south_33'
fileDir = ReHelper.replaceDir2(fileDir)
SaveasDocxBatch(fileDir)
print('the task is OK')
# pathDir = r'C:\Users\chenlu\Desktop\word Version\words'
# pathDir = ReHelper.replaceDir2(pathDir)
# listDirs = os.listdir(pathDir)
# for pathDirName in listDirs:
#     pathDir = PathHelper.CombinePathpurely(pathDir,pathDirName)
#     SaveasDocxBatch(pathDir,log)

print 2
