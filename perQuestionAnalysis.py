import json
import time, datetime
import csv
import os
import preProcess
import dataVis
from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
import pandas as pd


# from matplotlib import pyplot
import matplotlib.pyplot as plt
class channelData():
    def __init__(self):
        self.unixTime = None
        self.value = None
        self.Glabel= None
        self.qLabel = None

    

# lag 
def classifyEveryQuestionTime(Pgroup,currentTime):
    l = len(Pgroup)
    for i in range(0,l):
        last = i-1
        if(i == 0):
            #print()
            if(currentTime < (float(Pgroup[i].end)+7)):
                return True,Pgroup[i].label
        else:
            if(currentTime < (float(Pgroup[i].end+7)) and currentTime >= float(Pgroup[last].end+7)):
                print('debug classfy method ',currentTime,float(Pgroup[i].end))
                return True,Pgroup[i].label 
    return False

#     return data
def assignQuestionIndexTodata(wholeData,questionGroup):
    proDataset = []
    l = len(wholeData[0])
    print('whole data len:',l)
    for i in range(0,l):
        currentTime = wholeData[1][i]
        labelFlag,labelIndex = classifyEveryQuestionTime(questionGroup,currentTime)
        if(labelFlag):
            #print(labelIndex)
            proDataset.append(labelIndex)
            
    return proDataset

def clipQuestions(df):
    l = len(df['Label'])
    index = -1
    questionsArr = []
    for i in range (0,l):
        currentIndex = df['Question'][i]
        if(currentIndex > index):
            index= index+1
            questionsArr.append(i)
            # print(index,i)

    return questionsArr

def calculateMeanPerQuestion(df,questionAss):
    # print(questionAss)
    l = len(questionAss)
    tail = len(df['Label'])-1
    meanArr = preProcess.fnirData()
    labels = []
    for i in range(0,l-1):
        start = questionAss[i]
        end = questionAss[i+1]-1
        meanArr.G1.append(df['C1'][start:end+1].mean())
        # print(df['C1'][start:end+1].mean())
        meanArr.G2.append(df['C2'][start:end+1].mean())
        meanArr.G3.append(df['C3'][start:end+1].mean())
        meanArr.G4.append(df['C4'][start:end+1].mean())
        meanArr.G5.append(df['C5'][start:end+1].mean())
        meanArr.G6.append(df['C6'][start:end+1].mean())
        meanArr.G7.append(df['C7'][start:end+1].mean())
        meanArr.G8.append(df['C8'][start:end+1].mean())
        meanArr.G9.append(df['C9'][start:end+1].mean())
        meanArr.G10.append(df['C10'][start:end+1].mean())
        meanArr.G11.append(df['C11'][start:end+1].mean())
        meanArr.G12.append(df['C12'][start:end+1].mean())
        meanArr.G13.append(df['C13'][start:end+1].mean())
        meanArr.G14.append(df['C14'][start:end+1].mean())
        meanArr.G15.append(df['C15'][start:end+1].mean())
        meanArr.G16.append(df['C16'][start:end+1].mean())
        meanArr.G17.append(df['C17'][start:end+1].mean())
        meanArr.G18.append(df['C18'][start:end+1].mean())
        labels.append(int(df['Label'][start:end+1].mean()))
        # print('mean:',mean)

    start = questionAss[l-1]
    end = tail
    meanArr.G1.append(df['C1'][start:end+1].mean())
    meanArr.G2.append(df['C2'][start:end+1].mean())
    meanArr.G3.append(df['C3'][start:end+1].mean())
    meanArr.G4.append(df['C4'][start:end+1].mean())
    meanArr.G5.append(df['C5'][start:end+1].mean())
    meanArr.G6.append(df['C6'][start:end+1].mean())
    meanArr.G7.append(df['C7'][start:end+1].mean())
    meanArr.G8.append(df['C8'][start:end+1].mean())
    meanArr.G9.append(df['C9'][start:end+1].mean())
    meanArr.G10.append(df['C10'][start:end+1].mean())
    meanArr.G11.append(df['C11'][start:end+1].mean())
    meanArr.G12.append(df['C12'][start:end+1].mean())
    meanArr.G13.append(df['C13'][start:end+1].mean())
    meanArr.G14.append(df['C14'][start:end+1].mean())
    meanArr.G15.append(df['C15'][start:end+1].mean())
    meanArr.G16.append(df['C16'][start:end+1].mean())
    meanArr.G17.append(df['C17'][start:end+1].mean())
    meanArr.G18.append(df['C18'][start:end+1].mean())
    labels.append(int(df['Label'][start:end+1].mean()))
    return meanArr,labels

def plotMeans(means):
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax1.plot(range(0,153),means.G1)
    ax1.plot(range(0,153),means.G3)
    ax1.plot(range(0,153),means.G8)
    ax1.plot(range(0,153),means.G4)

    ax2 = fig.add_subplot(222)
    ax2.plot(range(0,153),means.G12)
    ax2.plot(range(0,153),means.G11)
    ax2.plot(range(0,153),means.G17)
    ax2.plot(range(0,153),means.G14)

    ax3 = fig.add_subplot(223)
    ax3.plot(range(0,153),means.G9)
    ax3.plot(range(0,153),means.G5)
    ax3.plot(range(0,153),means.G6)
    ax3.plot(range(0,153),means.G7)

    ax4 = fig.add_subplot(224)
    ax4.plot(range(0,153),means.G15)
    ax4.plot(range(0,153),means.G16)
    ax4.plot(range(0,153),means.G13)
    ax4.plot(range(0,153),means.G10)

    # plt.plot(range(0,153),means.G5)
    # plt.plot(range(0,153),means.G6)
    # plt.scatter(range(0,153),means.G3,subplots=True)
    # plt.scatter(range(0,153),means.G4,subplots=True)
    # plt.scatter(range(0,153),means.G5,subplots=True)
    # plt.scatter(range(0,153),means.G6,subplots=True)
    # plt.scatter(range(0,153),means.G7,subplots=True)
    # plt.scatter(range(0,153),means.G8,subplots=True)
    # plt.scatter(range(0,153),means.G9,subplots=True)
    # plt.scatter(range(0,153),means.G10,subplots=True)
    # plt.scatter(range(0,153),means.G11,subplots=True)
    # plt.scatter(range(0,153),means.G12,subplots=True)
    # plt.scatter(range(0,153),means.G13,subplots=True)
    # plt.scatter(range(0,153),means.G14,subplots=True)
    # plt.scatter(range(0,153),means.G15,subplots=True)
    # plt.scatter(range(0,153),means.G16,subplots=True)
    # plt.scatter(range(0,153),means.G17,subplots=True)
    # plt.scatter(range(0,153),means.G18,subplots=True)


    plt.ylabel('Means of per questions')
    plt.show()


def writeResultsToCsv(data,fileName):
    f = './dataset/questioncsv/lag/'+fileName+'.xlsx'
    data.to_excel(f, engine='xlsxwriter')  # doctest: +SKIP

def writeMeans(data,fileName,meanArr):
    a ={'Label':meanArr,
        'Question':range(0,153),
        'C1':data.G1,
        'C2':data.G2,
        'C3':data.G3,
        'C4':data.G4,
        'C5':data.G5,
        'C6':data.G6,
        'C7':data.G7,
        'C8':data.G8,
        'C9':data.G9,
        'C10':data.G10,
        'C11':data.G11,
        'C12':data.G12,
        'C13':data.G13,
        'C14':data.G14,
        'C15':data.G15,
        'C16':data.G16,
        'C17':data.G17,
        'C18':data.G18,
        }
    dfMeans = pd.DataFrame(a)
    f = './dataset/meancsv/lag7/'+fileName+'.xlsx'
    dfMeans.to_excel(f, engine='xlsxwriter')  # doctest: +SKIP

def main():
    FileName = 'P14'
    jsonAdd = './dataset/cleanJson/'+FileName+'.json'
    cvsAdd = FileName+'.csv'
    exAdd = FileName
    ######################## read data #####################################
    jsonData,patternGroup = preProcess.read_jsonData(jsonAdd)
    #######json , data['endTime']
    #print('jsonDara:',jsonData)
    #pStartArr,pEndArr = preProcess.getWholeKeyDownTime(jsonData)
    ####### arr , 153, per questions time
    #print('start:',pStartArr,len(pStartArr))
    timeGroups = preProcess.calculatePerQuestionTime(jsonData)
    ####### arr , 153, time structure .label,.start .end
    #print('time',timeGroups[20].label,len(timeGroups))

    participant,wholeData = dataVis.readDataFromcsv(cvsAdd)
    ######seriesData structure, lable,value, group 
    #print('parti:',participant.label)
    #######panda series [0]labels [1] time [2:19] channels
    #print('whole:',wholeData)
    

    ######################## process data #####################################
    proWholeData = assignQuestionIndexTodata(wholeData,timeGroups)
    # print('questionIndex len:',len(proWholeData))
    d ={'Label':wholeData[0],
        'Question':proWholeData,
        'TimeUnix':wholeData[1],
        'C1':wholeData[2],
        'C2':wholeData[3],
        'C3':wholeData[4],
        'C4':wholeData[5],
        'C5':wholeData[6],
        'C6':wholeData[7],
        'C7':wholeData[8],
        'C8':wholeData[9],
        'C9':wholeData[10],
        'C10':wholeData[11],
        'C11':wholeData[12],
        'C12':wholeData[13],
        'C13':wholeData[14],
        'C14':wholeData[15],
        'C15':wholeData[16],
        'C16':wholeData[17],
        'C17':wholeData[18],
        'C18':wholeData[19],
        }
    dfWholeData = pd.DataFrame(d)
    qsArr = clipQuestions(dfWholeData)
    # writeResultsToCsv(dfWholeData,'p10')
    perQuestionMeans,labels = calculateMeanPerQuestion(dfWholeData,qsArr)
    writeMeans(perQuestionMeans,exAdd,labels)
    #plotMeans(perQuestionMeans)
    # print(len(perQuestionMeans),qsArr,len(qsArr))
 
    #preProcess.classifyFdata()

if __name__ == "__main__":
	main()