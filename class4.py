import matplotlib.pyplot as plt
import numpy as np

y = ([1500000,1360000,1298000,1079000,1370000])
mylabels = (["Python","R","SQL","Java","Node JS"])
myexplode = [0.2,0,0,0,0]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True,autopct='%1.1f%%')
plt.legend()
plt.show()
