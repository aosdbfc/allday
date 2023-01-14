import numpy as np
import matplotlib.pyplot as plt

mu = 25
sigma1 = 6
sigma2 = 3

x = [mu + sigma1 * np.random.randn(1000)]
y1 = [mu + sigma1 * np.random.randn(1000)]
y2 = [mu + sigma2 * np.random.randn(1000)]
y3 = [ x + np.random.randn(1000)]

fig, ax = plt.subplots(1,3)

ax[0].scatter(x, y1)
ax[1].scatter(x, y2, color ='green')
ax[2].scatter(x, y3, color ='blue')

plt.show() 
