# -*- coding: utf-8 -*-
import os
#conbine the fileDir with the fileName
def CombinePathpurely(dataDir,dataName):
    return dataDir+"/"+dataName
def CombinefilePath(datafileDir, datafileName, dataExtension ='.pdf'):
    filePath = datafileDir + "/" + datafileName
    if os.path.isdir(filePath):
        pass
    else:
        fileNameParts = os.path.splitext(datafileName)
        if fileNameParts[1] <> '':
            pass
        else:
            filePath = datafileDir + "/" + datafileName + dataExtension
    #filePath = filePath.decode('utf-8')
    return filePath
def SplitfileName(dataFileName):
    listFilename = os.path.splitext(dataFileName)
    return listFilename[0],listFilename[1]


def JudgeFile(dataFilePath):
    if os.path.isfile(dataFilePath):
        return True
    else:
        return False

