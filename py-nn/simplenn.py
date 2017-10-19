from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import h5py

#based on tutorial from https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

# fix random seed for reproducibility
np.random.seed(7)
print('hi')

data = np.loadtxt('../data/sinedata.csv', delimiter=',', skiprows=1)
input = data[:, 0]
output = data[:, 1]
print(input)
print(output)



model = Sequential()
model.add(Dense(12, input_dim=1, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation= 'sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(input, output, epochs=5000, batch_size=1000)

model.save('simple-model.h5')

# >>> testx[:,0:4]
# array([[ 4,  6,  9, 20],
       # [ 1,  2,  3,  4]])

# G,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,IBB,HBP,SH,SF,GIDP
# 0,1 ,2,3,4 ,5 ,6 ,7  ,8 ,9 ,10,11,12 ,13 ,14,15,16