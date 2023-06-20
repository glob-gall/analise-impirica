af = float(input())

if(af <= 10000):
	
	vt = (5 * af)
	print(round(vt, 2))
	
else:
	vt = 50000 + ((af - 10000) * 4)
	print(round(vt, 2))