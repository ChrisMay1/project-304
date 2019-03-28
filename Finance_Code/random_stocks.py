import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import math
import random

profits = 0
losses = 0 
initial = 10000.00 
bank_account = initial
net_worth = 0.0
account = "sold"
style.use('ggplot')

start = dt.datetime(2018,01,01)
end = dt.datetime(2018,12,31)
ticker = 'SPY'

df = web.DataReader(ticker, 'yahoo', start, end)

def buy(count):
	global bank_account
	global account
	global shares
	global net_worth
	#~ print bank_account
	shares = math.floor(bank_account/float(df['Adj Close'][count]))
	bank_account -= shares*float(df["Adj Close"][count])
	net_worth = bank_account + shares*float(df["Adj Close"][count])
	account = "bought"
	# ~ print "buying shares is:", shares
	# ~ print "bank account is: ", bank_account
    
def sell(count):
	global bank_account
	global account
	global shares
	global net_worth
	# ~ print "Bank account is currently: ", bank_account
	# ~ print "# of shares is: ", shares
	bank_account += shares*float(df["Adj Close"][count])
	net_worth = bank_account + shares*float(df["Adj Close"][count])
	shares = 0
	account = 'sold'
	# ~ print "After Selling Bank account is: ", bank_account
	# ~ print "number of shares are: ", shares

def calculate_worth(count):
	global bank_account
	global shares
	global net_worth
	net_worth = bank_account + shares*float(df["Adj Close"][count])

def agent():
	i = 0
	global profits
	global losses
	global account
	global bank_account
	global net_worth
	global return_
	global count
	wX = []
	wY = []
	while i < len(df):
		# ~ print "Day: ", df.index[i], "Networth is: ", net_worth
		dummy = random.randint(0,1)
		if bank_account <= 0:
			losses += 1
			break
		if dummy == 1  and bank_account > 0 and account == 'sold':
			buy(i)
		if dummy == 0 and account == 'bought':
			sell(i)
		calculate_worth(i)
		wX.append(df.index[i])
		wY.append(net_worth)
		i +=1
	plt.plot(wX, wY)

	if net_worth > initial:
		profits += 1
		return_.append((net_worth/initial - 1)*100)
	else:
		losses += 1
		return_.append((net_worth/initial - 1)*100)
	# ~ print "***************************Round: ", count, "Networth is: ", net_worth
    
sampleSize = 1000
count = 1
return_ = []

while count < sampleSize:
    shares = 0
    bank_account = initial
    net_worth = 0.0
    account = 'sold'
    agent()

    count += 1

print "Profits are : ", profits
print "losses are : ", losses

average_return = np.mean(return_)
print "Average rate of return for" , sampleSize, "agents was", average_return, "%"

plt.axhline(10000, color = 'r')
plt.ylabel("Account Value")
plt.xlabel("date")
plt.show()



