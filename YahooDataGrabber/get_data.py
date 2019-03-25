import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web

class DataSys:
	
	def __init__(self, numstocks):
		
		if numstocks == 'all':
			N = 30
		else:
			N = numstocks
		
		start = datetime.datetime(2018, 1, 1)
		end = datetime.datetime(2019, 1, 1)

		symbols = pd.read_csv('../Finance_Code/Dow_30.csv')['Symbol']
		Nstocks = len(symbols)
		API = 'yahoo'

		print "Retriving", N, "stocks.."
		stocks = []
		available_symb = []
		for i in range(N):
			stocks.append(web.DataReader(symbols[i], API, start, end))
		print "Stocks retrieved:", symbols
		
		self.symbols = available_symb
		self.stocks = stocks
		self.length = len(stocks[0])
	
	def show_stocks(self):
		print self.symbols
	
	def retrieve_stockdata(self, stock):
		return web.DataReader(stock, API, start, end)

system = DataSys(3)

x = np.arange(system.length)

fig = plt.figure("the stocks")
ax1 = fig.add_subplot(111)

for i in range(3):
	ax1.plot(x, system.stocks[i]['Open'])

plt.show()
