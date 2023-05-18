#Valor de vendas de um funcionário.
vv = float(input("Valor de vendas de um funcionario: "))
if (vv > 1000):
	t = 1000 * 0.05 + (vv - 1000)*0.10
	print(round(t,2))
else:
	f = vv * 0.05
	print(round(f,2))