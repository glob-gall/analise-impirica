vendas= float(input('vendas: '))

if vendas<=1000:
	comissao= vendas*5/100
	
if vendas>1000:
	comissao= 1000*5/100+(vendas-1000)*10/100
	
print(round(comissao,2))

