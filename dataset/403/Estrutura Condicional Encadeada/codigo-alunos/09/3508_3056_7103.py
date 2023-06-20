a = float(input())
if a>=0 and a<=10000:
	custo = 6
	fert = 100
	valor = a * custo + fert
	print(round(valor,2))
elif a>=10000 and a<=20000:
		custo = 5.5
		fert = 150
		valor = a * custo + fert
		print(round(valor,2))
elif a>=20000 and a<=30000:
		custo = 5
		fert = 200
		valor = a * custo + fert
		print(round(valor,2))
elif a>30000:
		custo = 4.5
		fert = 250
		valor = a * custo + fert
		print(round(valor,2))