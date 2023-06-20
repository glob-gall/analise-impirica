area = float(input())

if (area >=0 and area <= 10000):
	c = 6
	f = 100
	valor = area*c + f
	print(round(valor, 2))
elif (area > 10000 and area <=20000):
	c = 5.50
	f = 150
	valor = area*c + f
	print(round(valor, 2))
elif (area > 20000 and area <= 30000):
	c = 5
	f = 200
	valor = area*c + f
	print(round(valor, 2))
elif (area > 30000):
	c = 4.50
	f=250
	valor = area*c + f
	print(round(valor, 2))
	
	
	