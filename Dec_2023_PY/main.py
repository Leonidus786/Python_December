# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./csv_files/username.csv')
print(df.to_string())

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
x = np.linspace(0, np.pi)
y2 = -x * 2
y_sin = np.sin(x)
y_cos = np.cos(x)
z = x ** 2 + x
ax1.plot(x, y_cos)
ax2.plot(x, z, 'co-', linewidth = 1, markersize = 2)
ax3.plot(x, y_sin, color = 'blue', marker = '+', linestyle = 'dashed')
ax4.plot(x, y2, 'm-.', markersize = 2)
plt.show()