h = float(input("Qual o tamanho da area? "))


if (0<h<10000):
	c = 6.0
	f = 100.0
elif (10000<h<20000):
	c = 5.50
	f = 150.0
elif (20000<h<30000):
	c = 5.0
	f = 200.0
elif (h>30000):
	c = 4.50
	f = 250.0
	
vt = h*c+f	
print(round(vt,2))
	
	