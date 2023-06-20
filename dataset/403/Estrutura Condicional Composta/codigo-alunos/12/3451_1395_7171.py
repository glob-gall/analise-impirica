#salario

vendas= float(input("Digite o valor de vendas:"))

if (vendas <=1000):
	comis= vendas *0.05
	
else:
	comis= (1000*0.05) + ((vendas - 1000) * 0.1)

print( round( comis, 2))
