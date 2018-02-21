
def withdraw(balance, value):
	print "Current balance = " + str(balance)
	
	if   value > balance:
		print "Can't give you all this money !!"

	elif value <= 0:
		print "More than zero plz!" 

	else:
		balance -= value
		while value > 0:
        
			if value >= 100:
				value -= 100
				print "give 100"

			elif value >= 50:
				value -= 50
				print "give 50"

			elif value >= 10:
				value -= 10
				print "give 10"
			elif value >= 5:
				value -= 5
				print("give 5")

			elif value < 5:
				print("give " + str(value))
				value = 0
	
		return balance
	
	

balance = 500
balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)