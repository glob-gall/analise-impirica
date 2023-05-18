a = float(input("area: "))

if (a >= 0):
	
	if (a <= 10000):
		
		c = 6
		f = 100
		
	if (a > 10000 and a <= 20000):
		
		c = 5.5
		f = 150
		
	if (a > 20000 and a <= 30000):
		
		c = 5
		f = 200
		
	if (a > 30000):
		
		c = 4.5
		f = 250
		
	
	
	v = (a * c) + f
	print (round(v, 2))
	