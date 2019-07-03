import urllib.request
import json, os

APIKEY = '8DV5XP4NBXHQO2PG'
ticker = 'TMO'

def import_web(ticker):
	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ticker+'&interval=1min&apikey='+APIKEY+'&outputsize=full&datatype=json'
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	return mystr

# ~ def partitionSave(ps,ticker):
	# ~ date = {}
	# ~ for i in ps:
		# ~ date[i[:10]] = 'date'
	# ~ for d in date.keys():
		# ~ tmp = {}
		# ~ for i in ps:
			# ~ if (i[:10] == d):
				# ~ tmp[i] = ps[i]
		# ~ if(os.path.isdir(d) == False):
			# ~ os.mkdir(d)
		# ~ fname = ticker + "_dann"
		# ~ try:
			# ~ with open(os.path.join(d,fname),'r') as f:
				# ~ t = json.load(f)
				# ~ for i in t:
					# ~ tmp[i] = t[i]
		# ~ except Exception as e:
			# ~ pass
		# ~ with open(os.path.join(d,fname), 'w') as f:
			# ~ json.dump(tmp,f)
			

def get_value(ticker):
	js = import_web(ticker)
	parsed_data = json.loads(js)
	ps = parsed_data['Time Series (1min)']
	print(ps)

get_value('GOOGL')


