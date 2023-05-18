a=float(input())

if(a>=0) and (a<10000):
	vt= a*6+100
	print(round(vt,2))

elif(a>10000)and(a<=20000):
	vt= a*5.50+150
	print(round(vt,2))
		
elif(a>20000)and(a<=30000):
	vt= a*5+200
	print(round(vt,2))
	
else:
	vt= a*4.50+250
	print(round(vt,2))