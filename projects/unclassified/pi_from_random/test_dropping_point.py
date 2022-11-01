from pylab import *
from matplotlib.animation import FuncAnimation
import random

fig = plt.figure(figsize=(8,6), dpi=150)
x = np.linspace(-2, 4.5, 250)

h=4
a=1
b=3

hlines(y=h, xmin=a, xmax=b, linewidth=1.5)
vlines(x=a, ymin=0, ymax=h, linewidth=1.5)
vlines(x=b, ymin=0, ymax=h, linewidth=1.5)

ylim(-2.5,10.5)
xlim(-2.5,4.5)
grid()

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

for i in range(10000):
    R1 = random.random()
    R2 = random.random()
    x0 = (b - a) * R1 + a
    y0 = h * R2
    ax.scatter(x0, y0, 10, color='red')
plt.show()