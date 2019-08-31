"""Simple matshow() example."""
import matplotlib.pyplot as plt
import numpy as np


# plt.matshow(samplemat((15, 35)))
rands = np.random.rand(10, 10)

f, axarr = plt.subplots(2, 2)
axarr[0, 0].matshow(rands)
axarr[0, 1].matshow(rands)
axarr[1, 0].matshow(rands)
axarr[1, 1].matshow(rands)

plt.show()
