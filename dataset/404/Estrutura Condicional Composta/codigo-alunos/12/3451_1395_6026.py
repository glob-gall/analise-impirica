vendas= float(input("Digite o valor: "))

if(vendas<=1000):
	c= vendas*0.05
else:
	v= vendas-1000
	c= (1000*0.05)+(v*0.10)
print(round(c,2))
