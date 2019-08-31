import numpy as np
import matplotlib.pyplot as plt
from random import randint

np.set_printoptions(suppress=True)

rands_1 = []
rands_2 = []
for i in range(100):
    rands_1.append(randint(0, 5))
    rands_2.append(randint(0, 5))

rands_1 = np.array(rands_1)
rands = np.concatenate((rands_1, rands_2))
print(rands)
# unique, counts = np.unique(rands, return_counts=True)

# bell curve
# x = np.random.normal(size = 10000)
# plt.hist(x, normed=True, bins=100)
# plt.ylabel('Probability');

plt.hist(rands_1)
# plt.show()
