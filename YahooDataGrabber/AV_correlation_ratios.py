import requests
import alpha_vantage
import json
import datetime as datetime
import time
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import style

style.use('ggplot')
API_URL = "https://www.alphavantage.co/query"
symbols = ['INTC', 'QRVO', 'TMO', 'XLE', 'XLU', 'Z', 'FB']
symbols = ['FB', 'INTC']
count = 0
history = []
for i in symbols:
    print i
    
for i in symbols:
    print i  
    data_1 = {"function": "TIME_SERIES_DAILY",
            "symbol": i,
            "interval": "daily",
            "outputsize": "full",
            "datatype": "json",
            "apikey": "BHU83C952GQ9GFX7"}
    
    time.sleep(10)
    response_data_1 = requests.get(API_URL, data_1)
    data_1= response_data_1.json()
    
    r_1 = (data_1['Time Series (Daily)'])
    keys_1 = (r_1.keys())
    keys_1 = sorted(keys_1) 
    history.append(i)
    count +=1
    
    for symbol in symbols:
        if symbol != i and symbol not in history:
            print "comparing", symbol  
            data_2 = {"function": "TIME_SERIES_DAILY",
                    "symbol": symbol,
                    "interval": "daily",
                    "outputsize": "full",
                    "datatype": "json",
                    "apikey": "BHU83C952GQ9GFX7"}
            
            time.sleep(10)
            response_data_2 = requests.get(API_URL, data_2)
            data_2= response_data_2.json()
            
            r_2 = (data_2['Time Series (Daily)'])
            keys_2 = (r_2.keys())
            keys_2 = sorted(keys_2)
            
            ratio = (data_1['Time Series (Daily)'])
            ratio_key = (ratio.keys())
            ratio_key = sorted(ratio_key)

            del keys_1[:len(keys_1)-150], ratio_key[:len(keys_1)-150]
            del keys_1[-1], keys_2[-1]
            
            ratio_index = []
            ratio_value = []
            for i in keys_1:
                ratio[i]['4. close'] = float(r_1[i]['4. close'])/float(r_2[i]['4. close'])
                ratio_index.append(i)
                ratio_value.append(ratio[i]['4. close'])


plt.plot(ratio_index, ratio_value, label = 'ratio')
plt.legend()
plt.show()       
    
    

    





