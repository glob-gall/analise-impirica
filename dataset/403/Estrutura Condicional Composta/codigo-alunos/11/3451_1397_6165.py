area = float(input("Qual o valor da area a ser fertilizada, em hectares: ")) 

if(area <= 10000):
	total = area*5
	print(round(total, 2))
else:
	restante = area-10000
	total = 10000*5+restante*4
	print(round(total, 2))