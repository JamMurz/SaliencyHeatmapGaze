import matplotlib.pyplot as plt
import numpy as np

X = ['Social Media','Web Browsing','Shopping','News']
three = [0.202,0.22,0.226,0.308]
four = [0.138,0.136,0.188,0.186]
five = [0.04,0.08,0.1,0.066]

change_t = [0.08,0.01,0.09,0.07]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, three, 0.2,label = '3g')
plt.bar(X_axis, four, 0.2, label = '4g')
plt.bar(X_axis + 0.2 , five, 0.2,label = '5g')  
plt.xticks(X_axis, X)
plt.xlabel("Website Categories")
plt.ylabel("Decrease in Load Time ")
plt.title("Perforamce based on category")
plt.legend()
plt.show()