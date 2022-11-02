import random

import matplotlib.pyplot as plt
import numpy as np

x = np.array([ random.uniform(0,100) for _ in range(100000)])
y = np.array([random.uniform(0,100) for _ in range(100000)])

for i in range(1000):
    plt.scatter(random.uniform(0,100), random.uniform(0,100))
plt.show()