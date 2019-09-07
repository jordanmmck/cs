import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 360, 0.1)
y1 = -1 * np.sqrt((x - 180)**2) + 180

plt.plot(x, y1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('')
plt.axis([0, 360, 0, 180])
plt.text(20, 150, r'$y=-√[(x-180)^2] + 180$')
plt.grid(True)
plt.show()
