import matplotlib.pyplot as plt
import numpy as np

x = (["Python","R","SQL","Java","Node JS"])
y = ([1500000,1360000,1298000,1079000,1370000])

plt.bar(x,y)
plt.xlabel("IT Technologies")
plt.ylabel("Annual Income")
plt.show()
