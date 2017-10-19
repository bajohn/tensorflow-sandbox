import numpy as np


# Let's make a simple math function (with no noise for now) and get a neural net to fit it.
out = 'x, sin(x)\n'

for x in range (0, 10000):
    arg = x/1000
    out+=  str(arg) + ',' + str(1/2+np.sin(x/1000)/2) + '\n'
    
  
print('done')
   
f = open('../data/sinedata.csv', 'w+')    

f.write(out)

f.close()
    


