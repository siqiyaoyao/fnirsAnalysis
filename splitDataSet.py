import json
import time, datetime
import csv
import os
import preProcess
import dataVis
from pandas import DataFrame
from pandas import TimeGrouper
import pandas as pd
from sklearn.model_selection import train_test_split

# read all docs from dataset documeny
def readWholeCSV(docName):
    Folder_Path = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/meancsv/'+ docName         
    
    os.chdir(Folder_Path)
    file_list = os.listdir()
    # file_list.remove('.DS_Store')
    print('doc list:', file_list)
    return file_list


# read data from csv 
def readDataFromcsv(add,fileName):
    reader = pd.read_csv(add+fileName,header=0)
    return reader

# delete certain group by label 
def deleteCertainGroup(wholeData,column,rows):
    df = wholeData[~wholeData[column].isin(rows)]
    # print(df)
    return df

def divideGroups(data):
    output = []
    for i in range(2,9):
        temp = data[data.Label.isin([i])]
        # print(temp)
        output.append(temp)
    print(len(output))
    return output

# pre process data
def cleanDataset(dataset):
    output = deleteCertainGroup(dataset,'Label',[1])
    # output = divideGroups(dataset)
    trainArr = splitData(output)
    for i in range(0,4):
        name = str(i)
        writeResultsToCsv(trainArr[i],name)
    return 

# transfer the data in to four sets, x_train, y_train, x_test, y_test
def splitData(data):
    train_data = data[['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18']]
    train_target = data[['Label']]
    X_train,X_test, y_train, y_test = train_test_split(train_data,train_target,test_size=0.4, random_state=8)
    # print(X_train)
    # print(y_test)
    output = []
    output.append(X_train)
    output.append(y_train)
    output.append(X_test)
    output.append(y_test)
    return output
    
# wrire dataframe to xlsx
def writeResultsToCsv(data,fileName):
    f = '/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/train/7/'+fileName+'.xlsx'
    data.to_excel(f, engine='xlsxwriter')  # doctest: +SKIP


def main():
    fileList = readWholeCSV('lag7')
    add = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/meancsv/lag7/'
    filename = fileList[0]  
    dataset = readDataFromcsv(add,filename)
    cleanDataset(dataset)
    #print(seriesGroups.groups[0],len(seriesGroups.groups))
    # allParicipants,allSets = getWholeParticipents(fileList)
    # g1,g2,g3,g4,g5,g6,g7,g8 = processPergroup(allSets,allParicipants)
    # #plotPerGroup(g1)
    # print(len(allParicipants))


    #preProcess.classifyFdata()

if __name__ == "__main__":
	main()