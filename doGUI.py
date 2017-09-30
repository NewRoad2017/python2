# -*- coding: utf-8 -*-
import sys

import wx
sys.path.append("D:/Applications/Python2/dataFileHelper")
sys.path.append("D:/Applications/Python2/generalFunction")
from dataFileHelper import PDFHelper2
from generalFunction import ReHelper,FileHelper
import os
#event
def Updatelb(datalb,dataList):
    for item in dataList:
        datalb.Append(item)

def OriL2MergeList(event):
    lbMergeList.Append(lbFolderList.GetStringSelection())
    lbFolderList.Delete(lbFolderList.GetSelection())

def MergeL2OriList(event):
    lbFolderList.Append(lbMergeList.GetStringSelection())
    lbMergeList.Delete(lbMergeList.GetSelection())
def Merge(event):
    listMerge = lbMergeList.GetStrings()
    print listMerge
    PDFHelper2.Mergepdf(fileDir, listMerge)
    FileHelper.DeleteFiles(fileDir, listMerge, ".pdf")
    #continue thing
    lbMergeList.Clear()
    lbFolderList.Clear()
    listFilesDir = FileHelper.GetDirfiles(fileDir)
    Updatelb(lbFolderList,listFilesDir)
#move to the otherFolder
def OriL2MoveList(event):
    lbMoveList.Append(lbFolderList.GetStringSelection())
    lbFolderList.Delete(lbFolderList.GetSelection())

def MoveL2OriList(event):
    lbFolderList.Append(lbMoveList.GetStringSelection())
    lbMoveList.Delete(lbMoveList.GetSelection())
def Move(event):
    listMove = lbMoveList.GetStrings()
    print listMove
    wfilePath = r"C:\Users\chenlu\Desktop\提交表\北极\6北"
    wfilePath = ReHelper.replacePath(wfilePath)
    FileHelper.MoveFiles(fileDir,listMove,".pdf",wfilePath)
    #continue operation
    lbMoveList.Clear()
    lbFolderList.Clear()
    listFilesDir = FileHelper.GetDirfiles(fileDir)
    Updatelb(lbFolderList, listFilesDir)

def test(event):
    print "OK"



#1.turn the '\' letter to '/' letter
fileDir = r'C:\Users\chenlu\Desktop\数据整理last\北极\6北'
fileDir = ReHelper.replacePath(fileDir)
listFilesinDir = os.listdir(fileDir)

app = wx.App()
window = wx.Frame(parent = None, title="registerdatasRescue", size=(800, 300))
panel = wx.Panel(window)

#1. lbFolderList
widthLB1 = 400
heightLB1 = 225
labelOriL = wx.StaticText(panel, label="Data Folder List", pos=(0, 0))
lbFolderList = wx.ListBox(panel, id = -1, pos = (0, 20), size = (widthLB1, heightLB1), choices=listFilesinDir)
widthLB1 = lbFolderList.GetMinWidth()
#button
widthBTN = 40
heightBTN = 25
btnOriL2MergeL = wx.Button(parent = panel, label ='>', pos=(widthLB1 + 10, 25), size=(widthBTN, heightBTN))
btnOriL2MergeL.Bind(wx.EVT_BUTTON, OriL2MergeList)
btnMergeL2OriL = wx.Button(parent = panel, label ='<', pos=(widthLB1 + 10, 50), size=(widthBTN, heightBTN))
btnMergeL2OriL.Bind(wx.EVT_BUTTON, MergeL2OriList)
btnMerge = wx.Button(parent = panel,label = 'Merge',pos=(widthLB1 + 5,75),size=(widthBTN+10,heightBTN))
btnMerge.Bind(wx.EVT_BUTTON,Merge)

btnOriL2MoveL = wx.Button(parent = panel, label ='>', pos=(widthLB1 + 10, 145), size=(widthBTN, heightBTN))
btnOriL2MoveL.Bind(wx.EVT_BUTTON, OriL2MoveList)
btnMoveL2OriL = wx.Button(parent = panel, label ='<', pos=(widthLB1 + 10, 170), size=(widthBTN, heightBTN))
btnMoveL2OriL.Bind(wx.EVT_BUTTON, MoveL2OriList)
btnMove = wx.Button(parent = panel,label = 'Move',pos=(widthLB1 + 5,195),size=(widthBTN+10,heightBTN))
btnMove.Bind(wx.EVT_BUTTON,Move)

#2. listBox
labelMergeL = wx.StaticText(panel, label="Merge List", pos=(widthLB1 +widthBTN+ 20, 0))
lbMergeList = wx.ListBox(panel, id = -1, pos = (widthLB1 +widthBTN+ 20, 20), size = (widthLB1, 100))
labelMoveL = wx.StaticText(panel, label="Move List", pos=(widthLB1 +widthBTN+ 20, 120))
lbMoveList = wx.ListBox(panel, id = -1, pos = (widthLB1 +widthBTN+ 20, 140), size = (widthLB1, 100))

window.Show(True)
app.MainLoop()

