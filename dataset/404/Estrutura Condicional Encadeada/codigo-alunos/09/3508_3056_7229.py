ac=float(input())

if(ac>=0):
	if(0<=ac<=10000):
		v=(ac*6)+100
		print(round(v,2))
	elif(ac>10000 and ac<=20000):
		v=(ac*5.50)+150
		print(round(v,2))
	elif(20000<ac and ac<=30000):
		v=(ac*5)+200
		print(round(v,2))
	elif(ac>30000):
		v=(ac*4.50)+250
		print(round(v,2))