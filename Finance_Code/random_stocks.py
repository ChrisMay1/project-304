import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import math
import random


style.use('ggplot')

start = dt.datetime(2019,01,01)
end = dt.datetime(2019,03,24)
ticker = 'SPY'

df = web.DataReader(ticker, 'yahoo', start, end)

df['9MA'] = df['Adj Close'].rolling(window = 9, min_periods = 0).mean() 
df['200MA'] = df['Adj Close'].rolling(window = 200, min_periods = 0).mean()

def buy(shares, count, bank_account):
    x = math.floor(bank_account/float(df['Adj Close'][count]))
    bank_account -= x*float(df["Adj Close"][count])
    y = 'bought'
    shares = x
    account = y
    print bank_account
    
def sell(shares, count, bank_account):
    shares
    bank_account += shares*float(df["Adj Close"][count])
    y = 'sold'
    account = y
    print bank_account

sampleSize = 10
count = 1

def agent(shares, bank_account):
    i = 0
    while i < len(df):
        dummy = random.randint(0,1)
        if dummy == 1 and account == 'sold':
            buy(shares, i, bank_account)
        if dummy == 0 and account == 'bought':
            sell(shares, i, bank_account)
        i +=1
    print bank_account
while count < sampleSize:
    shares = 0
    bank_account = 10000.00
    account = 'sold'
    agent(shares, bank_account)

    print count
    count += 1




