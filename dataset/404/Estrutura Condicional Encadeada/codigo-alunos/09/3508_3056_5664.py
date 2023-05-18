a= float(input('area: '))

if a>=0 and a<=10000:
	valor= a*6+100
	
elif 10000<a<=20000:
	valor= a*5.5+150
	
elif a>20000 and a<=30000:
	valor= (a*5)+200
	
elif a>30000:
	valor= a*4.5+250
	
print(round(valor,2))