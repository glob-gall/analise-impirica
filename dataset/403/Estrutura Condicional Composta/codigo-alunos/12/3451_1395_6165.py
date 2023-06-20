valorVendas = float(input("Qual o valor de vendas de um funcionario: ")) 

if(valorVendas <= 1000):
	total = valorVendas*0.05
	print(round(total, 2))
else:
	x = valorVendas - 1000
	total = x*0.10+1000*0.05
	print(round(total, 2))