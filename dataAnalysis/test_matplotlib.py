import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import numpy as np

index = list(range(1, 13))
values = list(range(3, 15))
plt.bar(index, values)
plt.plot(index, values, 'rD')
plt.plot(index, values, '+')
plt.title('Title')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()

t = np.arange(0., 4., 0.1)
plt.plot(t, t, t, t + 3, t, t ** 2, t, np.exp(t))
plt.show()

pl.plot(t, t, t, t + 3, t, t ** 2, t, np.exp(t))
pl.show()
