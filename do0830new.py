# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("D:/Applications/Python2/dataFileHelper")
from dataFileHelper import PDFHelper2
filePath = u'C:/Users/chenlu/Desktop/数据整理/南极/17/5_6.pdf'
pdf = PDFHelper2.PDFRead(filePath)
pdfPage = pdf.getPage(0)
print 2