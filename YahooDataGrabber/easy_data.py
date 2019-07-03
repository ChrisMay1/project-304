import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime as datetime

start = datetime.datetime(2018,2,01)
end = datetime.datetime(2019,5,19)
ticker = 'TMO'

df = web.DataReader(ticker, 'yahoo', start, end)

print df.head()
