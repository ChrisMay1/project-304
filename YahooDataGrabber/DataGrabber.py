import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web

class DataSys:
	
	def __init__(self, start, end, n_stocks = 1):
		
		if n_stocks == 'all':
			N = 30
		else:
			N = n_stocks

		symbols = pd.read_csv('../Finance_Code/Dow_30.csv')['Symbol']
		Nstocks = len(symbols)
		API = 'yahoo'

		print "Retriving", N, "stocks.."
		stocks = []
		available_symb = []
		for i in range(N):
			available_symb.append(symbols[i])
			stocks.append(web.DataReader(symbols[i], API, start, end))
		print "Stocks retrieved"
		
		self.symbols = available_symb
		self.stocks = stocks
	
	def get_open(self, stock_id, time):
		return self.stocks[stock_id]['Open'][time]
		
	def get_close(self, stock_id, time):
		return self.stocks[stock_id]['Close'][time]
	
	def length(self):
		return len(self.stocks[0])
	
	def get_symbols(self):
		return self.symbols
	
	def get_keys(self):
		return self.stocks[0].keys()
	
