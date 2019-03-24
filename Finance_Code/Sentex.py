import numpy as np
import random 
import matplotlib
import matplotlib.pyplot as plt
import time

lower_bust = 31.235
higher_profit = 63.208

sampleSize = 100
startingFunds = 10000
wagerSize = 100
wagerCount = 1000
broke_count	= 0

multiple_busts = 0.0
doubler_busts = 0.0
multiple_profits = 0.0
doubler_profits = 0.0

def rollDice():
	roll = random.randint(1,100)
	
	if roll == 100:
		#print roll, "Loss"
		return False
	elif roll <= 50:
		#print roll, "Loss"
		return False
	elif 100 > roll > 50:
		#print roll, "Win"
		return True
	
# ~ def doubler_bettor(funds, initial_wager, wager_count, color):
	# ~ value = funds
	# ~ wager = initial_wager
	# ~ global doubler_profits
	# ~ global doubler_busts
	# ~ global broke_count
	# ~ wX = []
	# ~ vY = []
	# ~ currentWager = 1
	# ~ previousWager = "Win"
	# ~ previousWagerAmount = initial_wager
	# ~ while currentWager <= wager_count:
		# ~ if previousWager == "Win":
			# ~ #print "won last one"
			# ~ if rollDice():
				# ~ value += wager
				# ~ #print value
				# ~ wX.append(currentWager)
				# ~ vY.append(value)
			# ~ else:
				# ~ value -= wager
				# ~ previousWager = "Loss"
				# ~ previousWagerAmount = wager
				# ~ wX.append(currentWager)
				# ~ vY.append(value)
				# ~ if value < 0:
					# ~ doubler_busts += 1
					# ~ break
		# ~ elif previousWager == "Loss":
			# ~ #print "we lost last one, we will double now"
			# ~ if rollDice():
				# ~ wager = previousWagerAmount*2			
				# ~ if (value - wager) < 0:
					# ~ wager = value
				# ~ value += wager 
				# ~ wager = initial_wager
				# ~ previousWager = "Win"
				# ~ wX.append(currentWager)
				# ~ vY.append(value)
			# ~ else:
				# ~ wager = previousWagerAmount*2
				# ~ if (value - wager) < 0:
					# ~ wager = value
				# ~ #print "we lost", wager
				# ~ value -= wager
				# ~ if value < 0:
					# ~ doubler_busts += 1
					# ~ break
				# ~ previousWager = "Loss"
				# ~ previousWagerAmount = wager
				# ~ wX.append(currentWager)
				# ~ vY.append(value)
		
		# ~ currentWager += 1
	# ~ plt.plot(wX, vY, color)
	# ~ if value > funds:
		# ~ doubler_profits += 1


# ~ def simple_bettor(funds, initial_wager, wager_count, color):
	# ~ value = funds
	# ~ wager = initial_wager
	# ~ global simple_profits
	# ~ global simple_busts
	# ~ global broke_count
	# ~ wX = []
	# ~ vY = []
	# ~ currentWager = 1
	# ~ while currentWager <= wager_count:
		# ~ if rollDice():
			# ~ value += wager
			# ~ wX.append(currentWager)
			# ~ vY.append(value)
		# ~ else:
			# ~ value -= wager
			# ~ wX.append(currentWager)
			# ~ vY.append(value)
		# ~ currentWager += 1	
	# ~ if value <= 0 :
		# ~ value = 0
		# ~ broke_count += 1
		# ~ simple_busts += 1
	# ~ #print "Funds:", value
	# ~ plt.plot(wX, vY, color)
	# ~ if value > funds:
		# ~ simple_profits += 1

def multiple_bettor(funds, initial_wager, wager_count):
	global multiple_busts
	global multiple_profits
	value = funds
	wager = initial_wager
	wX = []
	wY = []
	currentWager = 1
	previousWager = "Win"
	
	while currentWager <= wager_count:
		if previousWager == "Win":
			if rollDice():
				value += wager
				#print value
				# ~ wX.append(currentWager)
				# ~ wY.append(value)
			else:
				value -= wager
				previousWager = "Loss"
				previousWagerAmount = wager
				# ~ wX.append(currentWager)
				# ~ wY.append(value)
				if value < 0:
					multiple_busts += 1
					break
		elif previousWager == "Loss":
			if rollDice():
				wager = previousWagerAmount * random_multiple			
				if (value - wager) < 0:
					wager = value
				value += wager 
				wager = initial_wager
				previousWager = "Win"
				# ~ wX.append(currentWager)
				# ~ wY.append(value)
			else:
				wager = previousWagerAmount * random_multiple
				if (value - wager) < 0:
					wager = value
				value -= wager
				if value < 0:
					multiple_busts += 1
					break
				previousWager = "Loss"
				previousWagerAmount = wager
				# ~ wX.append(currentWager)
				# ~ wY.append(value)
		
		currentWager += 1
	# ~ plt.plot(wX, vY, color)
	if value > funds:
		multiple_profits += 1

while True:
	multiple_busts = 0.0
	multiple_profits = 0.0 
	multipleSampSize = 100000
	currentSample = 1
	random_multiple = random.uniform(1.4,1.85)
	
	while currentSample <= multipleSampSize:
		multiple_bettor(startingFunds, wagerSize, wagerCount)
		currentSample += 1

	if ((multiple_busts/multipleSampSize)*100.00 < lower_bust) and ((multiple_profits/multipleSampSize)*100.00 > higher_profit):
		print "#################################################"
		print "Found a winner, the multiple was", random_multiple
		print "Lower bust to beat", lower_bust
		print "Higher profit rate to beat:", higher_profit
		print "bust rate:", (multiple_busts/multipleSampSize)*100.00
		print "profit rate:", (multiple_profits/multipleSampSize)*100.00
		print "#################################################"
		time.sleep(2)
	
	else:
		print "**************************************************"
		print "Found a loser, the multiple was", random_multiple
		print "Lower bust to beat", lower_bust
		print "Higher profit rate to beat:", higher_profit
		print "bust rate:", (multiple_busts/multipleSampSize)*100.00
		print "profit rate:", (multiple_profits/multipleSampSize)*100.00
		print "**************************************************"

# ~ xx = 0

# ~ while xx < sampleSize:
	# ~ doubler_bettor(startingFunds, wagerSize, wagerCount, 'c')
	# ~ simple_bettor(startingFunds, wagerSize, wagerCount, 'k')
	# ~ xx += 1

# ~ print "simple Bettor bust chance:", (simple_busts/sampleSize)*100.00
# ~ print "Doubler Bettor bust chance:", (doubler_busts/sampleSize)*100.00

# ~ print "Simple Bettor profit chances:", (simple_profits/sampleSize)*100.00
# ~ print "Doubler Bettor profit cahnces:", (doubler_profits/sampleSize)*100.00

# ~ plt.axhline(0, color = 'r')
# ~ plt.ylabel("Account Value")
# ~ plt.xlabel("Wager Count")
# ~ plt.show()


