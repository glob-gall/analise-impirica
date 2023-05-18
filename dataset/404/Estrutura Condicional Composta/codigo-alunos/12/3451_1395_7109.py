vf = float(input("Valor de vendas de um funcionario: "))
if vf <= 1000:
	p1 = vf * 0.05
	print(round(p1,2))
else:
	m = vf - 1000
	n = vf - m
	p2 = (n * 0.05) + (m * 0.1)
	print(round(p2,2))