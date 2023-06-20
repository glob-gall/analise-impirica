vv = float(input())

if(vv <= 1000):
	
	vt = (vv * (5/100))
	print(round(vt, 2))
	
else:
	
	vt = (1000 * (5/100)) + ((vv - 1000) * (10/100))
	print(round(vt, 2))