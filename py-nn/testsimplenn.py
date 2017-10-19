import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from keras.models import load_model
#from keras.layers import Dense
import numpy as np
#import h5py


model = load_model('simple-model.h5')


# piplot uses format (x1, y1, param, x2, y2, param, ...)

xArr = []
yTrue = []
yPredict = []

for x in range (0, 10000):
    arg = x/1000
    xArr.append(arg)
    yTrue.append(np.sin(arg)/2+1/2)
    prediction = model.predict(np.array([arg]))[0][0]
    yPredict.append(prediction)
    #print('result: ' + str(prediction))
   
plt.plot(xArr, yTrue, '')
plt.plot(xArr, yPredict)
#plt.plot(xArr, yTrue, '', xArr, yPredict, '')

plt.savefig('../static/nn-out.png')
    
  