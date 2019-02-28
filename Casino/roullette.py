import numpy as np
import math
import random as rand
import matplotlib.pyplot as plt

period = 100
times = 100
initial = 100.0
bank = initial
results = []*period
bet = 5.0
j = 0 

while j <= period:
	array = [1]*times
	for i in range(times):
		array[i] = rand.randint(0,37)
	# ~ print j, 'Round'
	a = 0.0
	b = 0.0
	c = 0.0
	d = 0.0
	
	for i in range(len(array)):
		if bank <= 0:
			break
		if array[i] >= 1 and array[i] <= 12:		#win
			a = a + 1
			bank = bank + bet 
		if array[i] > 12 and array[i] <= 24:		#win
			b = b + 1
			bank = bank + bet 			
		if array[i] >= 25 and array[i] <= 36:		#loss
			c = c + 1
			bank = bank - 2*bet
		if array[i] == 0 or array[i] == 37:
			bank = bank - 2*bet
			d = d + 1
	results.append(bank)
	bank = initial 
	j = j + 1

positive = 0.0
negative = 0.0

for i in range(len(results)):
	if results[i] > initial:
		positive = positive + 1
	else:
		negative = negative + 1
		
print positive, negative
print 'made money percentage: ', positive/period*100
print 'lost money percentage: ', negative/period*100
	
t = np.arange(0,len(results),1)
plt.bar(t, results)
plt.title("Monte Carlo Roullette")
plt.xlabel("Trial #")
plt.ylabel("Value $")
plt.show()

