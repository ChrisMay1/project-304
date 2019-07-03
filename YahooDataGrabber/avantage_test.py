import urllib.request

APIKEY = '8DV5XP4NBXHQO2PG'

def import_web(ticker):
	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ticker+'&interval=60min&apikey='+APIKEY+'&outputsize=compact&datatype=json'
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	return mystr

ticker = 'TMO'
print(import_web(ticker))
