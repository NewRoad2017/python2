# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('D:/Applications/Python2/generalFunction')
from generalFunction import PathHelper,ReHelper
from shutil import copy


## to move file
# to move the file to another place
def MoveFile(dataFilePath,dataTargetfilePath):
    copy(dataFilePath,dataTargetfilePath)
    os.remove(dataFilePath)

# def MergeFiles(dataDir, dataTargetDir):
#     listFiles = GetDirfiles(dataDir)
#     for fileCurrent in listFiles:
#         filePath = PathHelper.CombinePathpurely(dataDir, fileCurrent)
#         if os.path.isfile(filePath):
#             tarFilePath = dataTargetDir+fileCurrent
#             MoveFile(filePath,tarFilePath)
#         else:
#             oriDir = PathHelper.CombinePathpurely(dataDir,fileCurrent)
#             MergeFiles(oriDir,dataTargetDir)


## to dulplicate file
# to dulplicate the file to another place
def DulplicateFile(dataOriPath,dataTarPath):
    tarPathparts = os.path.split(dataTarPath)
    copy(dataOriPath,dataTarPath)
    return "copy "+dataOriPath + " into "+tarPathparts[1]

#extract all the files with ".docx" and ".doc" in this dir to another file dir
def MergeFiles(dataOriDir, dataTarDir, dataExtensions,index):
    listFiles = GetDirfiles(dataOriDir)
    for fileCurrent in listFiles:
        oriDir = PathHelper.CombinePathpurely(dataOriDir, fileCurrent)
        if os.path.isfile(oriDir):
            listFileParts = os.path.splitext(fileCurrent)
            # if listFileParts[1] == dataExtensions:
            #     tarFilePath = PathHelper.CombinefilePath(dataTarDir, str(index), dataExtensions)
            #     DulplicateFile(oriDir, tarFilePath)
            #     index = index+1
            for extension in dataExtensions:
                if listFileParts[1] == extension:
                    tarFilePath = PathHelper.CombinefilePath(dataTarDir,str(index),extension)
                    DulplicateFile(oriDir, tarFilePath)
                    index = index+1
                    break
        else:
            print "to go into" + oriDir + str(index)
            index = MergeFiles(oriDir, dataTarDir,dataExtensions,index)
            print "out" + oriDir + str(index)
    return index

def DeleteFiles(dataFileDir,dataFileNames,dataExtension):
    for index in range(0,len(dataFileNames)):
        fileCurrent = dataFileNames[index]
        #fileCurrent = dataFileNames[index].decode("utf-8")
        filePath = PathHelper.CombinefilePath(dataFileDir, fileCurrent, dataExtension)
        os.remove(filePath)
        print "Delete File: "+ filePath

def GetDirfiles(dataFileDir):
    return  os.listdir(dataFileDir)


def RenameFile(dataFileDir,dataFilenameOri,dataFilenameLast):
    filePathOri = PathHelper.CombinefilePath(dataFileDir, dataFilenameOri)
    filePathLast = PathHelper.CombinefilePath(dataFileDir, dataFilenameLast)
    os.rename(filePathOri,filePathLast)


def BatchRenamefiles(dataFileDir,dataBatch):
    listFiles = GetDirfiles(dataFileDir)
    filesCount = len(listFiles)
    for index in range(0,filesCount):
        fileName= listFiles[index]
        fileNameLast = dataBatch["batchName"]+str(index)+dataBatch["batchEx"]
        RenameFile(dataFileDir,fileName,fileNameLast)

##
#the series of folder operations
def BatchCreatFolders(dataDir, dataCount, dataBeginnumber, dataInerterval, dataBatchName):
    for index in range(dataBeginnumber,dataBeginnumber+dataCount*dataInerterval):
        folderName = dataBatchName+str(index)
        folderPath = PathHelper.CombinePathpurely(dataDir, folderName)
        if os.path.exists(folderPath):
            pass
        else:
            os.mkdir(folderPath)








if __name__ == "__main__":
    pathDir = r'\\192.168.30.89\share\第33次南极考察原始数据、注册表'
    #pathDir = 'C:\Users\chenlu\Desktop\word Version\south_32'
    pathDir = ReHelper.replacePath(pathDir)
    tarDir = r'C:\Users\chenlu\Desktop\word Version\south_33'
    tarDir = ReHelper.replacePath(tarDir)
    # test = os.getcwd()
    # test = os.path.dirname(tarDir)
    # test_Dir = os.path.abspath(test)
    MergeFiles(pathDir,tarDir,['.docx','.doc'],0)
    #MergeFiles(pathDir, tarDir,'.docx',0)
    # os.listdir(pathDir)
    # print len(os.listdir(pathDir))
    print 2
