import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from BubbleSort import fillTable, checkIfSorted, sortTable

x_data = fillTable(10)
y_data = [0,1,2,3,4,5,6,7,8,9]

fig, ax = plt.subplots()
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)



def update(i):
	x_data = sortTable()
	#y_data = fillTable(10)
	return plt.bar(x_data, y_data)
    

animation = FuncAnimation(fig, func=update, frames=np.arange(0, 10, 0.1), interval=10)
plt.show()
