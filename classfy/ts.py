# -*- coding: utf-8 -*-
# Created on Tue Jan 16 20:52:46 2018
# @author: acer
# =====================================

"""Example module"""

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# """Simulated example"""
# def example_time_series():
#     random.seed(111)
#     rng = pd.date_range(start='2000', end='2100', period=209, freq='M')
#     ts = pd.Series(np.random.uniform(-10, 10, size=len(rng)), rng).cumsum()
#     ts.plot(c='b', title= "Example Time Series")
#     plt.show()
#     ts.head(10)

# """Training dataset with rnn model"""
# def training_rnn_model():
#     print("x")


# read data

def readDataFromcsv(fileName):
    # reader = pd.read_csv('sdataTest.csv',header=None)
    reader = pd.read_csv(r'/Users/siqiyaoyao/git/python3/fnirs/fnirsAnalysis/dataset/tsData/'+fileName,header=None)   
    return reader



# random.seed(111)
# rng = pd.date_range(start='2000', end='2017', period=209, freq='M')
# ts = pd.Series(np.random.uniform(-10, 10, size=len(rng)), rng).cumsum()
ts = readDataFromcsv('p12-3.csv')
ts.plot(c='b',title ="Participant 12 Channel 2 Phonological- letters Time Series")
plt.show()
print (ts.head(10))

TS_raw = np.array(ts)
TS = TS_raw[:8021]
num_periods = 40
f_horizon = 20
# x_data = TS[:(len(TS)-(len(TS)%num_periods))]
x_data = TS[1:8001]
x_batches = x_data.reshape(-1, 40, 1)
# y_data = TS[20:(len(TS)-(len(TS)%num_periods))+f_horizon]
y_data = TS[21:8021]
y_batches = y_data.reshape(-1, 40, 1)
print('xl',len(x_data))
print(x_batches.shape)
print(x_batches[0:2])

print('yl',len(y_data))
print(y_batches[0:1])
print(y_batches.shape)

# """Test function"""
def test_data(series, forecast, num_periods):
    test_x_setup = TS_raw[-(8000 + forecast):]
    testX = test_x_setup[:8000].reshape(-1, 40, 1)
    testY = TS_raw[-(8000):].reshape(-1, 40, 1)
    return testX, testY

X_test, Y_test = test_data(TS, f_horizon, num_periods)
print(X_test.shape)
# print(X_test)

tf.reset_default_graph()

num_periods = 40
inputs = 1
hidden = 100
output = 1

x = tf.placeholder(tf.float32, [None, num_periods, inputs])
y = tf.placeholder(tf.float32, [None, num_periods, output])

basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=hidden, activation=tf.nn.relu)
rnn_output, states = tf.nn.dynamic_rnn(basic_cell, x, dtype=tf.float32)

learning_rate = 0.001

stacked_rnn_output = tf.reshape(rnn_output, [-1, hidden])
stacked_outputs = tf.layers.dense(stacked_rnn_output, output)
outputs = tf.reshape(stacked_outputs, [-1, num_periods, output])

loss = tf.reduce_sum(tf.square(outputs - y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
training_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()

epochs = 160

with tf.Session() as sess:
    init.run()
    for ep in range(epochs):
        sess.run(training_op, feed_dict={x:x_batches, y:y_batches})
        if ep%100==0:
            mse = loss.eval(feed_dict={x:x_batches, y:y_batches})
            print(ep, "\tMSE:", mse)
    y_pred = sess.run(outputs, feed_dict={x:X_test})
    # print(y_pred)
    
plt.title("Forecast vs Actual of Participant 7 Channel 4 ", fontsize=14)
plt.plot(pd.Series(np.ravel(Y_test)), "bo", markersize=1)
plt.plot(pd.Series(np.ravel(y_pred)), "r.", markersize=1)
plt.legend(['Actual',"Forecast"],loc="upper left")
plt.xlabel("Sampling Interval (1/7.8125 s)")
plt.ylabel("Amplitude (a.u)")

plt.show()