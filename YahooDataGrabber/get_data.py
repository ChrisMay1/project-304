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

print("Done")
