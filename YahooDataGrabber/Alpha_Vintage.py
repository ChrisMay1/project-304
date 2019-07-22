import requests
import alpha_vantage
import json

API_URL = "https://www.alphavantage.co/query" 
symbols = ["INTC"]

for symbol in symbols:
        data = { "function": "TIME_SERIES_INTRADAY", 
        "symbol": symbol,
        "interval" : "1min",       
        "datatype": "json", 
        "apikey": "30W24DEQZXOVR1DG" } 
        response = requests.get(API_URL, data) 
        data = response.json()
        print(symbol)
        a = (data['Time Series (1min)'])        
        keys = (a.keys())
        for key in keys:
                print a[key]['4. close'] ,a[key]['5. volume']
        
        
