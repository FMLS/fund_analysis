#encoding=utf-8
import time

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdate
from matplotlib.animation import FuncAnimation

from funds.Fund import Fund


fund_obj = Fund('001986')
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'g', animated=True)

ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
plt.xticks(pd.date_range('2017-01-01','2017-02-02',freq='1min'))

def init():
    ax.set_xlim(0, 60 * 8)
    ax.set_ylim(-3, 3)

    return ln,

def update(frame):
    xdata.append(i)

plt.show()
