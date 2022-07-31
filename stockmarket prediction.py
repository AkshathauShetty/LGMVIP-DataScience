# -*- coding: utf-8 -*-
"""Copy of StockMarket.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11gWRzYUwyTg4sH4Uw7nL9ZXQkEwbgIAx
"""

import numpy as np 
import math 
import matplotlib.pyplot as plt 
import pandas as pd

"""data set link"""

dataset =  pd.read_csv('https://raw.githubusercontent.com/mwitiderrick/stockprice/master/NSE-TATAGLOBAL.csv') 
dataset

"""describe the data"""

dataset.describe()

dataset.tail

dataset.dtypes

dataset['Date'].value_counts()

dataset['High'].hist()

plt.figure(figsize=(20,8)) 
dataset.plot()

data = dataset.filter(['Close']) 
datasetval = dataset.values 
training_data_len =  math.ceil(len(dataset)*8) 
training_data_len

datset =  dataset.iloc[:, 0:5]

training_set = dataset.iloc[:,1:2].values 
training_set

"""Scaling the data set"""

from sklearn.preprocessing import MinMaxScaler 
scaler =MinMaxScaler(feature_range=(0,1)) 
data_training_scaled = scaler.fit_transform(training_set)

features_set = [] 
labels = [] 
for i in range (60,586) : 
  features_set.append(data_training_scaled[i-60:i, 0]) 
  labels.append(data_training_scaled[i,0])

features_set , labels=np.array(features_set), np.array(labels)

features_set = np.reshape (features_set, ( features_set.shape[0], features_set.shape[1], 1 )) 
features_set.shape

"""build lstm"""

import tensorflow as tf  
from tensorflow.python.keras.models import Sequential 
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import LSTM

model = Sequential()

model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(features_set, labels,  epochs = 50, batch_size =20)

data_tested = pd.read_csv('https://raw.githubusercontent.com/mwitiderrick/stockprice/master/NSE-TATAGLOBAL.csv') 
dat_test_processed = data_tested.iloc[:,1:2] 
dat_test_processed

"""Prediction """

data_total = pd.concat((dataset['Open'], dataset['Open']),axis = 0)

test_inp = data_total[len(data_total)-len(dataset)-60:].values 
test_inp.shape

test_inp = test_inp.reshape(-1,1) 
test_inp=  scaler.transform(test_inp)

test_features = [] 
for i in range(60 , 89): 
  test_features.append(test_inp[i-60:i,0])

test_features = np.array(test_features)
test_features = np.reshape(test_features,(test_features.shape[0],test_features.shape[1],1)) 
test_features.shape

predictions = model.predict(test_features)

predictions

x_train =  dataset[0:1256]
y_train = dataset[1:1257] 
print(x_train.shape) 
print(y_train.shape)

x_train

"""np.random.randn"""

np.random.seed(1)
np.random.randn(3,3)

"""a single nimber from the normaldistributon"""

np.random.normal(1)

"""5 numbers from the normal distribution"""

np.random.normal(5)

np.random.seed(42)
np.random.normal(size = 1000 , scale = 100).std()

"""Plot the results"""

plt.figure(figsize=(18,6)) 
plt.title("stock market proce prediction") 
plt.plot(data_tested['Close']) 
plt.xlabel('Date', fontsize=18)
plt.ylabel('total trade quality', fontsize=18)
plt.show()



"""analyze the closing price from dataframe"""

dataset["Turnover (Lacs)"] = pd.to_datetime(dataset.Date) 
dataset.index= dataset["Turnover (Lacs)"]  
plt.figure(figsize=(20,10))  
plt.plot(dataset["Turnover (Lacs)"],label="close price hits")