value= 483
high_balance=500
if value < high_balance:
	x= [int(i) for i in str(value)]
	hunbreds= x[0]* "give 100\n"
	print hunbreds
	tens= x[1] 
	if tens>5:
		print "give 50"
		print int(tens-5) * "give 10\n"
	else:
		print tens * "give 10\n"
	dollers = x[2]
	
	if dollers>5:
		print "give 5"
		print "give "+ str(int(dollers-5))
	else:
		print "give "+ str(dollers)
else:
	print "higher than expected. Please enter a number less than 500"	
