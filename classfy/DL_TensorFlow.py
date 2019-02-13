import sys
sys.version

import tensorflow as tf 
import pandas as pd
import numpy as np 
import os
import matplotlib
import matplotlib.pyplot as plt 
import random
# % matplotlib inline
import tensorflow as tf 
import shutil
import tensorflow.contrib.learn as tflearn
import tensorflow.contrib.layers as tflayers
from tensorflow.contrib.learn.python.learn import learn_runner
import tensorflow.contrib.metrics as metrics
import tensorflow.contrib.rnn as rnn
#TF Version
print (tf.__version__)

# import data
random.seed(111)
rng = pd.date_range(start='2000',periods=209,freq='M')
ts = pd.Series(np.random.uniform(-10,10,size=len(rng)),rng).cumsum()
ts.plot(c='b',title ="Example Time Series")
plt.show()
print (ts.head(10))

# convert data into array
TS = np.array(ts)
num_periods = 20
f_horizon = 1
x_data = TS[:(len(TS)-(len(TS)%num_periods))]
x_batches = x_data.reshape(-1,20,1)

y_data = TS[1:(len(TS)-(len(TS)%num_periods))+f_horizon]
y_batches = y

