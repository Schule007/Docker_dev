import random

randomlist = []

for i in range(0,10):
    n = random.random()    
    randomlist.append(n)

print(randomlist)

from matplotlib import pyplot as plt
plt.plot(randomlist)
plt.show()
