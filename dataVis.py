from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
import pandas as pd
from matplotlib import pyplot
import os


import csv

class seriesData():
    def __init__(self):
        self.label = None
        self.unixTime = None
        self.groups = []

def readDataFromcsv(fileName):
    # reader = pd.read_csv('sdataTest.csv',header=None)
    reader = pd.read_csv(r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/finaldata/'+fileName,header=None)
    
    seriesGroups = seriesData()
    seriesGroups.label =reader[0]
    seriesGroups.unixTime = reader[1]
    #print(len(reader[2]))
    for i in range(0,18):# test 
        index = i + 2
        #print(reader[index])
        seriesGroups.groups.append(reader[index])    
    return seriesGroups,reader

def plotAllLabels(groups):
    labels = DataFrame()
    for index,g in enumerate(groups):
        labels[index] = g

    labels.plot(subplots=True, legend=False)
    pyplot.show()

def plotTotalSum(groups):
    groups[18].plot()
    pyplot.show()

def findGroupIndex(groups):
    arr = []
    current = -1
    for index,g in enumerate(groups):
        #print(g)
        if(g != current):
            current = g
            arr.append(index)
            print('debug',index,g)
    return arr

def groupData(indexArr,groups):
    dataGroups = []
    for i in range(0,8):
        perGroup = []
        if(i != 7):
            start = indexArr[i]
            end = indexArr[i+1]-1     
        else:
            start = indexArr[i]
            end = len(groups[0])
        #print('debug groups:',start,end)
        # for g in groups:
        #     perGroup.append(g[start:end])  
        #print('per group:',perGroup[0])
        dataGroups.append(groups[start:end])
        print('total group:',len(dataGroups))
    return dataGroups
        

def plotPerLabelsKde(groups):
    labels = DataFrame()
    for index,g in enumerate(groups):
        labels[index] = g

    labels.plot(subplots=True, legend=False,ind='kde')
    pyplot.show()
    
def baiscStaticValue(labels):
    # median = labels[2].median()
    # mean = labels[2].mean()
    # std = labels[2].std()
    # mode = labels[2].mode()[0]
    # print('channels:',2,'median:',median,'mean:',mean,'std:',std,'modes:',mode)
    for i in range(2,20):
        if(i != 13):
            median = labels[i].median()
            mean = labels[i].mean()
            std = labels[i].std()
            mode = labels[i].mode()[0]
            print('channels:',i-1,'median:',median,'mean:',mean,'std:',std,'modes:',mode)



def hist(labels):
    #baiscStaticValue(labels)
    labels[2].hist()
    labels[3].hist()
    labels[4].hist()
    labels[5].hist()
    labels[6].hist()
    labels[7].hist()
    labels[8].hist()
    labels[9].hist()
    labels[10].hist()
    labels[11].hist()
    labels[12].hist()
    #labels[13].hist()
    labels[14].hist()
    labels[15].hist()
    labels[16].hist()
    labels[17].hist()
    labels[18].hist()
    labels[19].hist()

    pyplot.show()

def plotKde(labels):
    labels[2].plot(kind='kde')
    labels[3].plot(kind='kde')
    labels[4].plot(kind='kde')
    labels[5].plot(kind='kde')
    labels[6].plot(kind='kde')
    labels[7].plot(kind='kde')
    labels[8].plot(kind='kde')
    labels[9].plot(kind='kde')
    labels[10].plot(kind='kde')
    labels[11].plot(kind='kde')
    labels[12].plot(kind='kde')
    #labels[13].plot(kind='kde')
    labels[14].plot(kind='kde')
    labels[15].plot(kind='kde')
    labels[16].plot(kind='kde')
    labels[17].plot(kind='kde')
    labels[18].plot(kind='kde')
    labels[19].plot(kind='kde')
    pyplot.show()

def readWholeJsons():
    Folder_Path = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/data/jsondata/'          #要拼接的文件夹及其完整路径，注意不要包含中文
    
    #修改当前工作目录
    os.chdir(Folder_Path)
    #将该文件夹下的所有文件名存入一个列表
    file_list = os.listdir()
    print('doc list:', file_list)

def main():
    DataSet_series,wholeSet = readDataFromcsv('p14.cvs')
    # print(wholeSet.head())
    # indexArr = findGroupIndex(DataSet_series.label)
    # labelGroups = groupData(indexArr,wholeSet)
    # #print('debug group data:',labelGroups[7])
    # #plotKde(labelGroups[7])
    # #hist(labelGroups[3])
    # baiscStaticValue(labelGroups[6])
    #plotPerLabelsKde(labelGroups[2:19])
    # readWholeJsons()

    plotAllLabels(DataSet_series.groups)
    #plotTotalSum(DataSet_series.groups)
    # DataSet_series.groups[0].plot()
    # pyplot.show()

    # lines = list(csv.reader(open('sdataTest.csv')))
    # header,values = lines[0],lines[1]
    # print(header,values)

    # series = Series.from_csv('sdataTest.csv', header=-1)
    # print(series.head(2))

if __name__ == "__main__":
	main()