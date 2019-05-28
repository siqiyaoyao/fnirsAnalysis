
from pandas import Series
from pandas import DataFrame




doc = r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/LSTM/feature_engineering/'
filename = 'daily-min-temperatures.csv'
fileAdd = doc+filename
#  tansfer raw data ro Pandas series with header
series = Series.from_csv(fileAdd, header=0)
#  tansfer series ro dataframe 
dataframe = DataFrame()
dataframe['month'] = [series.index[i].month for i in range(len(series))]
dataframe['day'] = [series.index[i].day for i in range(len(series))]
dataframe['temperature'] = [series[i] for i in range(len(series))]
print(dataframe.head(5))
