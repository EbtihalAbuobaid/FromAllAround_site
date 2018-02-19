value= 483
while value < 500:
	x= [int(i) for i in str(value)]
	a= x[0]* "give 100\n"
	print a
	b= x[1] 
	if b>5:
		print "give 50"
		print int(b-5) * "give 10\n"
	else:
		print b * "give 10\n"
	c= x[2]
	if b>5:
		print "give 5"
		print "give "+ str(int(b-5))
	else:
		print "give "+ str(int(b-5))
	break