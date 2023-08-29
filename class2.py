import matplotlib.pyplot as plt
import numpy as np

y = ([22.2,17.6,8.8,7.7,6.7])
mylabels = (["Java","Python","PHP","C","c++"])
myexplode = [0,0.2,0,0,0]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True,autopct='%1.1f%%')
plt.legend()
plt.axis('equal')
plt.show()
