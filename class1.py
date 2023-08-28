import matplotlib.pyplot as plt
import numpy as np

x = (["Java","Python","PHP","C","c++"])
y = ([22.2,17.6,8.8,7.7,6.7])

plt.bar(x,y)
plt.xlabel("Programing Language")
plt.ylabel("Popularity")
plt.show()
