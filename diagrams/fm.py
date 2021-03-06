import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 30.0, 0.01)
zeroes = [3] * 500
ones = [1] * 500
f = np.array((ones + zeroes) * 3)
s = np.cos(f*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.xlim(0, 30)
plt.ylim(-1.5,1.5)
plt.show()
