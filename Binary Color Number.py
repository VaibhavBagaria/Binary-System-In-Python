import matplotlib.pyplot as plot
import random
#b=random.random()
#c="%.1f" %(b)
#a=int(c)
#print(b)
a=0.3
print(a)
data=[
     [0,0,0,0,0,0,0,0],
     [0,0,0,a,a,0,0,0],
     [0,0,a,0,0,a,0,0],
     [0,0,a,0,0,a,0,0],
     [0,0,0,a,a,0,0,0],
     [0,0,a,0,0,a,0,0],
     [0,0,a,0,0,a,0,0],
     [0,0,0,a,a,0,0,0]
     ]

plot.imshow(data, cmap='winter')
plot.show()