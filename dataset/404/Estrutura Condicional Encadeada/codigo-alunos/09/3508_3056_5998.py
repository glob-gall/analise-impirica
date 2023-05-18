a = float(input("area do gramado: "))

if (0<=a<=10000):
	#custo:
	c = 6
	
	#fertilizante:
	f = 100
	
elif (10000<a<=20000):
	c=5.50
	f=150
elif (20000<a<=30000):
	c=5.0
	f=200
else:
	c=4.50
	f=250
	
valor = round((a*c)+f,2)
print(valor)