import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import copy
from matplotlib import style
import csv
import time


start = dt.datetime(1994, 01, 01)
end = dt.datetime(2018, 12, 11)

df = web.DataReader('SPY', 'yahoo', start, end)

X = [1]* int(len(df))

def return_percentage(t):
	a = float(((df['Adj Close'][-1] - df['Adj Close'][t])/df['Adj Close'][t])*100)

	return a
	
t = 0
order = True

while order != False:
		
		a = df['Adj Close'][t]
		X[t] = return_percentage(t)
		
		if df['Adj Close'][t] == df['Adj Close'][-1]:
			print df['Adj Close'][-1]
			print 'done'
			order = False
		t = t + 1
		
for i in range(0, len(X)):
	if X[i] == 1:
		X[i] = np.nan

		
plt.plot(df.index, X, label = 'Percent Return')
plt.plot(df.index, df['Adj Close'], label = 'SPY')
plt.title('SPY Returns')
plt.xlabel('Date Sold')
plt.ylabel('% Return')
plt.legend()
plt.show()

