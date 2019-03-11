<<<<<<< HEAD
import pandas as pd
import pandas_datareader.data as web
import datetime
=======
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2018, 1, 1)
end = dt.datetime(2019, 2, 27)

ticker = 'INTC'

df = web.DataReader(ticker, 'yahoo', start, end)

print(df.tail())

plt.plot(df.index, df['Adj Close'])
plt.title(ticker)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
>>>>>>> b44df6e4f7f596c45e30d871680467cc006cb9b9

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
