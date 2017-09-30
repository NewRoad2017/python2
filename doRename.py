# -*- coding: utf-8 -*-
import os
fileDir = u"D:/Projects/Chinare/datarescue/中国极地扫描陈璐整理/南极/28次南极考察注册提交表"
srcFileName = "9"
tarFileName1 = u"王湾浮游纤毛虫丰度和生物量及其对其全球变暖的响应"
tarFileName2 = u"王湾浮游纤毛虫丰度和生物量及其对其全球变暖的响应"
os.rename(fileDir+"/pdf"+srcFileName+".pdf",fileDir+"/"+tarFileName1+"-"+tarFileName2+".pdf")