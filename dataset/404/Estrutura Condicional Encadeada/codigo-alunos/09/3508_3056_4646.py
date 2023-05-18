ac = float(input("area coberta"))
if(ac>=0):
	if(ac>=0 and ac<=10000):
		v= ac*6+100
		print(round(v,2))
	elif(ac>=10000 and ac<=200000):
		v= ac*5.5+150
		print(round(v,2))
	elif(ac>=200000 and ac<=30000):
		v = ac*5+200
		print(round(v,2))
	else:
		v = ac*4.5+250
		print(round(v,2))
else:
	print("invalido")
	
	