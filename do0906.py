# -*- coding: utf-8 -*-
import sys
sys.path.append("D:/Applications/Python2/generalFunction")
from generalFunction import ReHelper,FileHelper

fileDIR= r'C:\Users\chenlu\Desktop\MakeUp\data_register_table\exp_north\2北_2'
fileDIR = ReHelper.replacePath(fileDIR)
fileBatch = {}
fileBatch["batchName"] = "2b_2_"
fileBatch["batchEx"] = '.pdf'
FileHelper.BatchRenamefiles(fileDIR,fileBatch)