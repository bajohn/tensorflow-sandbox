from keras.models import Sequential
from keras.layers import Dense
import numpy as np

#based on tutorial from https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

# fix random seed for reproducibility
np.random.seed(7)
print('hi')

data = np.loadtxt('../static/30batting.csv', delimiter=',', skiprows=1, usecols=range(5,22))
input = np.concatenate((data[:, 0:7], data[:, 8:17]), axis=1)
output = data[:,7]
print(input)
print(output)







model = Sequential()
model.add(Dense(12, input_dim=16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation= 'sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(input, output, epochs=150, batch_size=10)

# >>> testx[:,0:4]
# array([[ 4,  6,  9, 20],
       # [ 1,  2,  3,  4]])

# G,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,IBB,HBP,SH,SF,GIDP
# 0,1 ,2,3,4 ,5 ,6 ,7  ,8 ,9 ,10,11,12 ,13 ,14,15,16