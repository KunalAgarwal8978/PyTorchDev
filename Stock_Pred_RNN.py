import pandas as pd
import numpy as np
import torch
from torch import nn
dataset=pd.read_csv('Google_Stock_Price_train.csv')
test_dataset=pd.read_csv('Google_Stock_Price_train.csv')

training_data=dataset.iloc[:,1:2].values
test_data=test_dataset.iloc[:,1:2].values
x_train=[]
y_train=[]


from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(-1,1))
training_data=scaler.fit_transform(training_data)
print(training_data.size)

for i in range(60,1257):
    x_train.append(training_data[i-60:i,0])
    y_train.append(training_data[i,0])

x_train,y_train=np.array(x_train),np.array(y_train)
print(x_train.shape)
x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
print(x_train.shape)



complete_data=pd.concat((dataset['Open'],test_dataset['Open']),axis=0)

inputs=complete_data[len(complete_data)-len(test_dataset)-60:].values
inputs=inputs.reshape(-1,1)
inputs=scaler.transform(inputs)
x_test=[]
for i in (60,80):
    x_test.append(inputs[i-60:i,0])
x_test=np.array(x_test)
x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

MyModel=Sequential()
MyModel.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
MyModel.add(Dropout(0.2))
MyModel.add(LSTM(units=50, return_sequences=True))
MyModel.add(Dropout(0.2))
MyModel.add(LSTM(units=50, return_sequences=True))
MyModel.add(Dropout(0.2))
MyModel.add(LSTM(units=50, return_sequences=False))

MyModel.add(Dense(units=1))
MyModel.compile(optimizer='RMSProp',loss='mean_squared_error')

MyModel.fit(x_train,y_train,epochs=100,batch_size=32)

predictes_prices=MyModel.predict(x_test)
predictes_prices=scaler.inverse_transform(predictes_prices)

import matplotlib.pyplot as plt

plt.plot(predictes_prices, color='red')
plt.plot(test_data, color='blue')
#plt.show()

print(predictes_prices)
print(test_data)