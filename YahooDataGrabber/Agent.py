import DataGrabber
import numpy as np
import matplotlib.pyplot as plt
import Tkinter as tk
import datetime

np.random.seed()

class agent:
	
	def __init__(self, StockData, money = 10000, shares = 0):
		self.money = money
		self.shares = shares
		self.StockData = StockData

	# buy a particular number of shares of stock at some time
	def buy(self, n_shares, time):
		self.shares += n_shares
		self.money -= self.StockData.get_open(0, time)
		
	# sel a particular number of shares of stock at some time
	def sell(self, n_shares, time):
		self.shares -= n_shares
		self.money += self.StockData.get_open(0, time)

	# what is my net worth at this time?
	def net_worth(self, time):
		return self.money + self.shares * self.StockData.get_open(0, time)

	def random_buysell(self, time):
		r = np.random.choice([0, 1])
		if r == 0:
			self.buy(1, t)
		if r == 1:
			self.sell(1, t)

# What is the date range of the data?
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2019, 1, 1)

# Set up a stock or stocks to simulate with (n_stocks is 1 by default)
S = DataGrabber.DataSys(start, end)
time = np.arange(S.length())

# Create an agent
Mark = agent(S)
NetWorth = []
Shares = []

# For the length of time of the stock, have the agent buy and sell
for t in time:
	Mark.random_buysell(t)
	NetWorth.append(Mark.net_worth(t))
	Shares.append(Mark.shares)

fig = plt.figure()
ax = fig.add_subplot(121)

x = np.arange(S.length())

index = 0
ax.plot(x, S.stocks[index]['Open'], label = S.symbols[index])
ax.legend(loc = 'best')

ax1 = fig.add_subplot(122)
ax1.plot(x, NetWorth, label = "Mark Net Worth")
ax1.legend(loc = 'best')

plt.show()
