value= 483
high_balance=500
if value < high_balance:
	x= [int(i) for i in str(value)]
	Hunbreds= x[0]* "give 100\n"
	print Hunbreds
	Tens= x[1] 
	if Tens>5:
		print "give 50"
		print int(Tens-5) * "give 10\n"
	else:
		print Tens * "give 10\n"
	Dollers = x[2]
	
	if Dollers>5:
		print "give 5"
		print "give "+ str(int(Dollers-5))
	else:
		print "give "+ str(Dollers)
else:
	print "higher than expected. Please enter a number less than 500"	
