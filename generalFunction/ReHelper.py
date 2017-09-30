# -*- coding: utf-8 -*-
import re

#替换函数
def subString(dataStr,dataPattern,dataReplace):
    newString = re.sub(dataPattern,dataReplace,dataStr)
    return newString
# replace the origin place path to the ultimate place path
def replacePath(dataStr):
    '''
    :keyword general usage
    :keyword replace '\' to '/'
    :param dataStr:
    :return:
    '''
    strConcrete = subString(dataStr,"\\\\","/")
    strConcrete = strConcrete.decode('utf-8')
    return strConcrete
def replaceDir2(dataStr):
    '''
    :keyword for win32com(2)
    :keyword repalce '\' to '\\'
    :param dataStr:
    :return:
    '''
    strConcrete = subString(dataStr,r"\\",r'\\')
    strConcrete = strConcrete.decode('utf-8')
    strConcrete = strConcrete + "\\" #??I still really can't understand
    return strConcrete