
from pandas import Series
from pandas import DataFrame
from pandas import concat

def readData(fileAdd):
    series = Series.from_csv(fileAdd, header=0)
    return series

def GroupFeatures(series):
    dataframe = DataFrame()
    dataframe['month'] = [series.index[i].month for i in range(len(series))]
    dataframe['day'] = [series.index[i].day for i in range(len(series))]
    dataframe['temperature'] = [series[i] for i in range(len(series))]
    print(dataframe.head(5))

# short lag
def LagFeatures(series,lags,c1,c2):
    temps = DataFrame(series.values)
    dataframe = concat([temps.shift(lags), temps], axis=1)
    dataframe.columns = [c1, c2]
    print(dataframe.head(5))

# long lag
def shiftFeatures(series):
    temps = DataFrame(series.values)
    dataframe = concat([temps.shift(3), temps.shift(2), temps.shift(1), temps], axis=1)
    dataframe.columns = ['t-3', 't-2', 't-1', 't+1']
    print(dataframe.head(5))

def Rollingwindow(series):
    temps = DataFrame(series.values)
    width = 3
    shifted = temps.shift(width-1)
    window = shifted.rolling(window = width)
    dataframe = concat([window.min(),window.mean(),window.max(),temps],axis=1)
    dataframe.columns = ['min','mean','max','t+1']
    print(dataframe.head(5))



# file address 
doc = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/LSTM/feature_engineering/'
filename = 'daily-min-temperatures.csv'
fileAdd = doc+filename

#  tansfer raw data ro Pandas series with header
series = Series.from_csv(fileAdd, header=0)

# #  tansfer series ro dataframe 
# dataframe = DataFrame()
# dataframe['month'] = [series.index[i].month for i in range(len(series))]
# dataframe['day'] = [series.index[i].day for i in range(len(series))]
# dataframe['temperature'] = [series[i] for i in range(len(series))]
# print(dataframe.head(5))

# # lag feature
# temps = DataFrame(series.values)
# dataframe = concat([temps.shift(1), temps], axis=1)
# dataframe.columns = ['t-1', 't+1']
# print(dataframe.head(5))

shiftFeatures(series)
Rollingwindow(series)