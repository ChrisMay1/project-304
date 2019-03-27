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
		available_data = []
		available_symb = []
		for i in range(N):
			available_symb.append(symbols[i])
			available_data.append(web.DataReader(symbols[i], API, start, end))
		print "Stocks retrieved"
		
		self.symbols = available_symb
		self.data = available_data
	
	def get_open(self, stock_id, time):
		return self.data[stock_id]['Open'][time]
		
	def get_close(self, stock_id, time):
		return self.data[stock_id]['Close'][time]
		
	def get_column(self, stock_id, key):
		return self.data[stock_id][key]
	
	def length(self):
		return len(self.data[0])
	
	def get_symbol(self, index):
		return self.symbols[index]
	
	def get_keys(self):
		return self.data[0].keys()
	
