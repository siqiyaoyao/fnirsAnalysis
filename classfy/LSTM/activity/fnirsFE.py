
from pandas import Series
from pandas import DataFrame
from pandas import concat

# long lag
def shiftFeatures(series):
    temps = DataFrame(series.values)
    dataframe = concat([temps.shift(39), temps.shift(38), temps.shift(37), temps.shift(36), temps.shift(35), temps.shift(34), temps.shift(33),temps.shift(32), temps.shift(31), temps.shift(30),
    temps.shift(29), temps.shift(28), temps.shift(27), temps.shift(26), temps.shift(25), temps.shift(24), temps.shift(23),temps.shift(22),temps.shift(21), temps.shift(20), 
    temps.shift(19), temps.shift(18), temps.shift(17), temps.shift(16), temps.shift(15), temps.shift(14), temps.shift(13),temps.shift(12),temps.shift(11), temps.shift(10), 
    temps.shift(9), temps.shift(8), temps.shift(7), temps.shift(6), temps.shift(5), temps.shift(4), temps.shift(3),temps.shift(2), temps.shift(1), temps], axis=1)
    dataframe.columns = ['t-39', 't-38', 't-37', 't-36','t-35', 't-34', 't-33', 't-32','t-31', 't-30', 
    't-29', 't-28', 't-27', 't-26','t-25', 't-24', 't-23', 't-22','t-21', 't-20', 
    't-19', 't-18', 't-17', 't-16','t-15', 't-14', 't-13', 't-12','t-11', 't-10', 
    't-9', 't-8', 't-7', 't-6','t-5', 't-4', 't-3', 't-2','t-1', 't-0',  ]
    print(dataframe.head(40))
    return dataframe

def Rollingwindow(series):
    temps = DataFrame(series.values)
    width = 40
    shifted = temps.shift(width-1)
    window = shifted.rolling(window = width)
    dataframe = concat([window.min(),window.mean(),window.max(),temps],axis=1)
    dataframe.columns = ['min','mean','max','t+1']
    print(dataframe.head(5))

# file address 
doc = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/LSTM/activity/fnirs/rawData/'
filename = '9.csv'
fileAdd = doc+filename
output = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/LSTM/activity/fnirs/rawData/output/'
fileOuts = output + filename
#  tansfer raw data ro Pandas series with header
series = Series.from_csv(fileAdd, header=0)
outDataFrame = shiftFeatures(series)

outDataFrame.to_csv(fileOuts)