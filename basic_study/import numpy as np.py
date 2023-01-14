import numpy as np
import matplotlib.pyplot as plt

mu1, sigma1 = 10, 2
mu2, sigma2 = -6, 3

standard_chart = np.random.randn(10000)
chart1 = mu1 + sigma1 * np.random.randn(10000)
chart2 = mu2 + sigma2 * np.random.randn(10000)

plt.figure()
plt.hist(standard_chart, bins = 50, alpha = 0.4)
plt.hist(chart1, bins = 50 , alpha = 0.4)
plt.hist(chart2, bins = 50, alpha =0.4 )

plt.show() 