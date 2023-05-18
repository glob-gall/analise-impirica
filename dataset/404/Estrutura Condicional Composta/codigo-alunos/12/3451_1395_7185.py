vvend = float(input("Digite o valor de vendas de um funcionario: "))
if (vvend <= 1000):
	por = vvend * 0.05
	print (round(por, 2))
else:
	ex = vvend - 1000
	por = (1000 * 0.05) + (ex * 0.10)
	print (round(por, 2))
