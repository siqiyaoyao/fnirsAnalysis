import json
import time, datetime
import csv
import os
import preProcess
import dataVis
from pandas import DataFrame
from pandas import TimeGrouper
import pandas as pd
from matplotlib import pyplot


def readWholeCSV(docName):
    Folder_Path = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/'+ docName          #要拼接的文件夹及其完整路径，注意不要包含中文
    
    #修改当前工作目录
    os.chdir(Folder_Path)
    #将该文件夹下的所有文件名存入一个列表
    file_list = os.listdir()
    file_list.remove('.DS_Store')
    print('doc list:', file_list)

    return file_list
def getWholeParticipents(fileList):
    allGroupData =[]
    allDataSet =[]
    for file in fileList:
        seriesGroups,dataSet = dataVis.readDataFromcsv(file)
        allGroupData.append(seriesGroups)
        allDataSet.append(dataSet)
    return allGroupData,allDataSet

def processPergroup(allSets,allParicipants):
    l = len(allParicipants)
    participants_label_arr = []
    g1 = []
    g2 = []
    g3 =[]
    g4 = []
    g5 = []
    g6 = []
    g7 = []
    g8 =[]
    for i  in range(0,l):# debug 1
        indexList = dataVis.findGroupIndex(allParicipants[i].label)
        group_label = dataVis.groupData(indexList,allSets[i]) # 0-19 0 group 1 time 2-19 channel 
        #normalizeData_devide(group_label)
        g1.append(group_label[0]) # 0-19 
        g2.append(group_label[1])
        g3.append(group_label[2])
        g4.append(group_label[3])
        g5.append(group_label[4])
        g6.append(group_label[5])
        g7.append(group_label[6])
        g8.append(group_label[7])

        #participants_label_arr.append(group_label)
    return g1,g2,g3,g4,g5,g6,g7,g8

def normalizeData_devide(groups):
    labelArr =[]
    for index,data in enumerate(groups): # 8 groups,  data [0] groupindex [1] time [2:19] channel
        n = len(data)
        groupIndex = data[0].mean()
        print(n,data[0].mean())


# def normalizeData_score(data):

def plotPerGroup(group):
    labels1 = DataFrame()
    labels2 = DataFrame()
    labels3 = DataFrame()
    labels4 = DataFrame()
    labels5 = DataFrame()
    labels6 = DataFrame()
    labels7 = DataFrame()
    labels8 = DataFrame()
    labels9 = DataFrame()
    labels10 = DataFrame()
    labels11 = DataFrame()
    labels12 = DataFrame()
    labels13 = DataFrame()
    labels14= DataFrame()
    labels15 = DataFrame()
    labels16 = DataFrame()
    labels17 = DataFrame()
    labels18 = DataFrame()
    for index,g in enumerate(group):
        labels1[index] = g[2]
        labels2[index] = g[3]
        labels3[index] = g[4]
        labels4[index] = g[5]
        labels5[index] = g[6]
        labels6[index] = g[7]
        labels7[index] = g[8]
        labels8[index] = g[9]
        labels9[index] = g[10]
        labels10[index] = g[11]
        labels11[index] = g[12]
        labels12[index] = g[13]
        labels13[index] = g[14]
        labels14[index] = g[15]
        labels15[index] = g[16]
        labels16[index] = g[17]
        labels17[index] = g[18]
        labels18[index] = g[19]


    labels1.plot(subplots=False, legend=False)
    labels2.plot(subplots=False, legend=False)
    labels3.plot(subplots=False, legend=False)
    labels4.plot(subplots=False, legend=False)
    labels5.plot(subplots=False, legend=False)
    labels6.plot(subplots=False, legend=False)
    labels7.plot(subplots=False, legend=False)
    labels8.plot(subplots=False, legend=False)
    labels9.plot(subplots=False, legend=False)
    labels10.plot(subplots=False, legend=False)
    labels11.plot(subplots=False, legend=False)
    labels12.plot(subplots=False, legend=False)
    labels13.plot(subplots=False, legend=False)
    labels14.plot(subplots=False, legend=False)
    labels15.plot(subplots=False, legend=False)
    labels16.plot(subplots=False, legend=False)
    labels17.plot(subplots=False, legend=False)
    labels18.plot(subplots=False, legend=False)
    pyplot.show()
    
def main():
    print('test')
    fileList = readWholeCSV('finaldata')
    #print(seriesGroups.groups[0],len(seriesGroups.groups))
    allParicipants,allSets = getWholeParticipents(fileList)
    g1,g2,g3,g4,g5,g6,g7,g8 = processPergroup(allSets,allParicipants)
    #plotPerGroup(g1)
    print(len(allParicipants))


    #preProcess.classifyFdata()

if __name__ == "__main__":
	main()