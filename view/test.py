import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from funds.Fund import Fund

# animation function.  This is called sequentially
#def animate(i):
#    data = np.random.random((255, 255))
#    im.set_array(data)
#    return [im]
#
#print animate(1)
#anim = animation.FuncAnimation(fig, animate, frames=200, interval=60, blit=True)
#plt.show()

#plt.axis([0, 100, 0, 1])
#plt.ion()
#
#for i in range(100):
#    y = np.random.random()
#    plt.plot(i, y)
#    plt.pause(0.01)

"""
A simple example of an animated plot
"""
fund_obj = Fund('001986')
y = [float(item['jj_lggz']) for item in fund_obj.get_daily_data()]
x = [x + 1 for x in xrange(len(y))]
plt.axis([1, len(y) + 1, 0.9, 1.6])
plt.plot(x,y)
plt.show()


#fig, ax = plt.subplots()
#
#x = np.arange(0, 1)
#print x
#line, = ax.plot(x, np.sin(x))
#
#
#def animate(i):
#    line.set_ydata(np.sin(x + i/10.0))  # update the data
#    return line,
#
#
## Init only required for blitting to give a clean slate.
#def init():
#    line.set_ydata(np.ma.array(x, mask=True))
#    return line,
#
#ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
#                              interval=25, blit=True)
#plt.show()
