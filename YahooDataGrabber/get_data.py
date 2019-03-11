import pandas as pd
import pandas_datareader.data as web
import datetime

import numpy as np
import matplotlib.pyplot as plt

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2019, 1, 1)

symbols = ['AAPL', 'AMZN', 'GOOG', 'ALL']
API = 'yahoo'

stocks = {}
for stock in symbols:
	stocks[stock] = web.DataReader(stock, API, start, end)

N = len(stocks['AMZN'])
x = np.arange(N)

fig = plt.figure("the stocks")
ax1 = fig.add_subplot(111)

for stock in symbols:
	print stock
	ax1.plot(x, stocks[stock]['Open'])

plt.show()
