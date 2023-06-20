a = float(input("Area: "))
if a>=0:
	if 0 <= a <=10000:
		v1 = a*6 + 100
		print(round(v1,2))
	elif 1000 <a <= 20000:
		v2 = a*5.50+150
		print(round(v2,2))
	elif 20000<a<=30000:
		v3 = a*5+200
		print(round(v3,2))
	else:
		v4 = a*4.50+250
		print(round(v4,2))		