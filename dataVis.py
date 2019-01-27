from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
import pandas as pd
from matplotlib import pyplot

import csv

class seriesData():
    def __init__(self):
        self.label = None
        self.unixTime = None
        self.groups = []

def readDataFromcsv():
    # reader = pd.read_csv('sdataTest.csv',header=None)
    reader = pd.read_csv('./testPlot/P3.csv',header=None)
    seriesGroups = seriesData()
    seriesGroups.lable =reader[0]
    seriesGroups.unixTime = reader[1]
    for i in range(0,19):# test 
        index = i + 2
        #print(reader[index])
        seriesGroups.groups.append(reader[index])    
    return seriesGroups

def plotAllLabels(groups):
    labels = DataFrame()
    for index,g in enumerate(groups):
        labels[index] = g

    labels.plot(subplots=True, legend=False)
    pyplot.show()

def plotTotalSum(groups):
    groups[18].plot()
    pyplot.show()

def main():
    DataSet_series = readDataFromcsv()
    #plotAllLabels(DataSet_series.groups)
    plotTotalSum(DataSet_series.groups)
    # DataSet_series.groups[0].plot()
    # pyplot.show()

    # lines = list(csv.reader(open('sdataTest.csv')))
    # header,values = lines[0],lines[1]
    # print(header,values)

    # series = Series.from_csv('sdataTest.csv', header=-1)
    # print(series.head(2))

if __name__ == "__main__":
	main()