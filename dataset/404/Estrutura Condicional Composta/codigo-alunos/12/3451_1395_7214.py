vv = float(input("Qual o valor de vendas? "))

if (vv<=1000):
	p = 0.05*vv
	print(round(p,2))	
else:
	a = vv - 1000
	p = (1000*0.05) + (a*0.10)
	print(round(p,2))