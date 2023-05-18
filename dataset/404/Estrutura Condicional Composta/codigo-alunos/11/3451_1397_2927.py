x = float(input("hectares: "))
if(x<=10000):
	valor= x*5
	print(round(valor,2))
else:
	y= x-10000
	total= 50000+y*4
	print(round(total,2))