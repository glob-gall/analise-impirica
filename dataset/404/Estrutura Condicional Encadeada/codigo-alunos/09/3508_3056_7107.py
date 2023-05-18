af = float(input())

if( af > 0 ):
	
	if( af > 0 and af <= 10000):
		c = 6
		f = 100
		
	elif( af > 10000 and af <= 20000):
		c = 5.50
		f = 150
		
	elif( af > 20000 and af <= 30000):
		c = 5
		f = 200
		
	else:
		c = 4.50
		f = 250
		
	vt = (af * c) + f
	
	print(round(vt, 2))