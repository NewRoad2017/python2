# -*- coding: utf-8 -*-
import sys
sys.path.append("D:/Applications/Python2/dataFileHelper")
sys.path.append("D:/Applications/Python2/generalFunction")
from dataFileHelper import PDFHelper2
from generalFunction import ReHelper,PathHelper



fileDir = r'D:\Projects\Chinare\nextcloud\极地考察历史数据抢救\极地考察实施计划\南极'
fileDir = ReHelper.replacePath(fileDir)
fileNames = [u'33.第33次南极考察现场实施计划--集合版.pdf']
wfileName = ""
pdfWrite = PDFHelper2.PDFWrite()
for index in range(0,len(fileNames)):
    fileName = fileNames[index]
    filePath = PathHelper.CombinePathpurely(fileDir, fileName)
    pdfRead = PDFHelper2.PDFRead(filePath)
    for pageindex in range(232,295):
        pdfRead.getPage(pageindex)
        pdfWrite.addPage(pdfRead.pdfPage)
    if index == 0:
        wfileName = fileName
    else:
        wfileName = wfileName+fileName[2:]
pdfWrite.fileWrite(PathHelper.CombinefilePath(fileDir,wfileName+"test",".pdf"))