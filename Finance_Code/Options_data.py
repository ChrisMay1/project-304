import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import timedelta
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
import csv
import time

plt.style.use('ggplot')

start = dt.datetime(2018, 1, 01)
end = dt.datetime(2019, 03, 06)

now = dt.datetime(2019, 03, 06)
expiration = dt.datetime(2019, 03, 15)

ticker = 'INTC'

df = web.DataReader(ticker, 'yahoo', start, end) 

# stock price
#exercise price
#Time to maturity
#Annual risk-free interest rate
#Annualized volatility

T = expiration
t = now
td = T-t
td = float(td.days)
print td

S = 52.95
K = 55.0
r = .0125
v = 23.54
#call option
d_1 = (1/(v*np.sqrt(td)))*(np.log(S/K) + (r + (v**2)/2)*(td))

d_2 = d_1 - v*np.sqrt(td)

PV = K*np.exp(-r*(td))

u = df['Adj Close'][-250:].mean()
print u
x = np.arange(-100, 100, 0.1)
# ~ d = (1/(v*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-u)/v)**2)

C = (1/(v*np.sqrt(2*np.pi)))*np.exp(-0.5*((d_1-u)/v)**2)*S - (1/(v*np.sqrt(2*np.pi)))*np.exp(-0.5*((d_2-u)/v)**2)*PV
print C

plt.plot(x, K*np.exp(-r*x))
plt.show()



