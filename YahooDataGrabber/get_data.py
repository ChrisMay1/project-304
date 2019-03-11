import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 1, 1)

symbols = pd.read_csv('../Finance_Code/Dow_30.csv')['Symbol']
API = 'yahoo'

stock = web.DataReader(symbols[0], API, start, end)

data = stock['Open']

N = len(data)
x = np.arange(N)

y = np.fft.fft(data)


fig = plt.figure("the stocks")
ax1 = fig.add_subplot(111)

ax1.plot(x, y)

plt.show()
