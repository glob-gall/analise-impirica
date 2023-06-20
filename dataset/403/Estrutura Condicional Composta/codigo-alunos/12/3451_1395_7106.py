vendas = float(input("Quantidade de vendas:  "))
din = 1000
if vendas<= din:
	valor = (vendas*0.05)
	print(round(valor, 2))
	
else:
	valor = (din*0.05)
	rest = (vendas-din)*0.10
	total = (valor+rest)
	print(round(total, 2))