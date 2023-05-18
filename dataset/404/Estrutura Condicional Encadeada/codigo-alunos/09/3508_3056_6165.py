area = float(input("Digite o tamanho da area: "))

if(area >=0):
	if(0 <= area <= 10000):
		valor = area*6+100
		print(round(valor,2))
	elif(10000 < area <= 20000):
		valor = area*5.50+150
		print(round(valor,2))
	elif(20000 < area <= 30000):
		valor = area*5+200
		print(round(valor,2))
	elif(area > 30000):
		valor = area*4.50+250
		print(round(valor,2))