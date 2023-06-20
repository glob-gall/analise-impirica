a = float(input("Area:  "))


if a <=10000:
	valor = a*5
	print(round(valor, 2))
	
else:
	ini = a - 10000
	dez = 10000*5
	sob = ini*4
	soma = dez+sob
	print(round(soma, 2))