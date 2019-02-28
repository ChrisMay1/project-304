import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2018, 01, 01)
end = dt.datetime(2019, 02, 27)

ticker = 'INTC'

df = web.DataReader(ticker, 'yahoo', start, end)

print df.tail()

print("Done")
