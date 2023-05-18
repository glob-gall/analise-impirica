area = float(input("Area a ser fertilizada: "))
if (0<=area<=10000):
	v = area * 6 + 100
	print(round(v,2))
elif (10000<area<=20000):
	v = area * 5.5 + 150
	print(round(v,2))
elif (20000<area<=30000):
	v = area * 5 + 200
	print(round(v,2))
elif (30000<area):
	v = area * 4.5 + 250
else:
	print("Erro")