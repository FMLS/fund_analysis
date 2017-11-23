#encoding=utf-8
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from funds.Fund import Fund

from matplotlib.animation import FuncAnimation

fund_obj = Fund('001986')

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'g', animated=True)


def init():
    ax.set_xlim(0, 400)
    ax.set_ylim(0.8, 1.6)

    ax.set_xlabel('days')
    ax.set_ylabel('nav')
    return ln,

i = 1
def update(frame):
    xdata.append(i)
    ydata.append(frame['nav'])
    ln.set_data(xdata, ydata)
    global i
    i = i + 1
    return ln,

ani = FuncAnimation(fig, update, frames=fund_obj.get_daily_data(),
                    init_func=init, blit=True, interval=50)
plt.show()

#x = [1,2,3]
#y = [5,7,4]
#
#x2 = [1,2,3]
#y2 = [10,14,12]
#plt.plot(x, y, label='First Line')
#plt.plot(x2, y2, label='Second Line')
#
#plt.xlabel('Plot Number')
#plt.ylabel('Important var')
#plt.title('Interesting Graph\nCheck it out')
#plt.legend()
#plt.show()
