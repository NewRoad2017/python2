# -*- coding: utf-8 -*-
import sys
sys.path.append("D:/Applications/Python2/dataFileHelper")
sys.path.append("D:/Applications/Python2/generalFunction")
from dataFileHelper import PDFHelper2
from generalFunction import ReHelper,FileHelper,PathHelper
# 拆分单元格
fileDir = r"D:\Projects\Chinare\datarescue\中国极地扫描陈璐整理\南极\25抽取"
fileDir = ReHelper.replacePath(fileDir)
dirFiles = FileHelper.GetDirfiles(fileDir)
for fileName in dirFiles:
    filepath = PathHelper.CombinefilePath(fileDir, fileName)
    if PathHelper.JudgeFile(filepath):
        fileNameOnly = PathHelper.getFileNameOnly(fileName)
        pdfRead = PDFHelper2.PDFRead(filepath)
        for pageindex in range(0,pdfRead.pdfReader.getNumPages()):
            pdfRead.getPage(pageindex)
            #dirPath = os.path.dirname(filePath)
            wfilePath = PathHelper.CombinefilePath(fileDir, fileNameOnly + "_" + str(pageindex), ".pdf")
            pdfWriter = PDFHelper2.PDFWrite()
            pdfWriter.addPage(pdfRead.pdfPage)
            pdfWriter.fileWrite(wfilePath)
        pdfRead.readFile.close()
print "OK"
FileHelper.RenameFile("ddd")

#filePath = u"D:/Projects/Chinare/datarescue/中国极地扫描陈璐整理/南极/31次南极考察数据注册表 提交表/30次越冬11.pdf"