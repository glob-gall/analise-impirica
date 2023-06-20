a=float(input())

if(a>=0):
	if(a>0 and a<=10000):
		v=(a*6)+100
		print(round(v,2))
	elif(a>10000 and a<=20000):
		v=(a*5.50)+150
		print(round(v,2))
	elif(a>20000 and a<=30000):
		v=(a*5)+200
		print(round(v,2))
	else:
		v=(a*4.50)+250