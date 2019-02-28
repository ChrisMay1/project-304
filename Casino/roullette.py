import numpy as np
import math
import random as rand
import matplotlib.pyplot as plt

period = 1000
times = 1000
array = [1]*times
bank = 1000.0
results = []*period
bet = 5.0
j = 0 

while j <= period:
	for i in range(times):
		array[i] = rand.randint(0,37)
	print j, 'Round'
	a = 0.0
	b = 0.0
	c = 0.0
	d = 0.0
	
	for i in range(len(array)):
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
	bank = 100.0
	j = j + 1

t = np.arange(0,len(results),1)
plt.bar(t, results)
plt.title("Monte Carlo Roullette")
plt.xlabel("Trial #")
plt.ylabel("Value $")
plt.show()

