# -*- coding: utf-8 -*-
#from pyPdf import pdf
import pyPdf.pdf
import  sys
sys.path.append('D:/Applications/Python2/generalFunction')
from generalFunction import PathHelper

class PDFRead:
    def __init__(self,filePath):
        self.filePath = filePath
        self.readFile = file(self.filePath, "rb")
        self.pdfReader = PdfFileReader(self.readFile)
    def getPage(self, dataIndex):
        self.pdfPage = self.pdfReader.getPage(dataIndex)



class PDFWrite:
    def __init__(self):
        self.pdfWriter = PdfFileWriter()

    def addPage(self, datapdfPage):
        self.pdfWriter.addPage(datapdfPage)

    def fileWrite(self,filePath):
        self.filePath = filePath
        self.writeFile = file(self.filePath, "wb")
        self.pdfWriter.write(self.writeFile)
        self.writeFile.close()

def Mergepdf(dataFileDir,dataFileNames):
    pdfWrite = PDFWrite()
    wfileName = ''
    pdfReads = []
    for index in range(0, len(dataFileNames)):
        fileName = dataFileNames[index]
        #fileName=fileName = dataFileNames[index].decode("utf-8")
        fileNameOnly = PathHelper.getFileNameOnly(fileName)
        filePath = PathHelper.CombinefilePath(dataFileDir, fileName)
        pdfRead = PDFRead(filePath)
        pdfReads.append(pdfRead.readFile)
        pdfRead.getPage(0)
        pdfWrite.addPage(pdfRead.pdfPage)
        if index == 0:
            wfileName = fileNameOnly
        else:
            wfileName = wfileName + '+'+fileNameOnly
    wfilePath = PathHelper.CombinefilePath(dataFileDir, wfileName)
    pdfWrite.fileWrite(wfilePath)
    for pdfread in pdfReads:
        pdfread.close()



if __name__ == '__main__':
    pp = PDFRead(r'D:\Projects\Chinare\nextcloud\Nextcloud Manual.pdf')
    print 2
