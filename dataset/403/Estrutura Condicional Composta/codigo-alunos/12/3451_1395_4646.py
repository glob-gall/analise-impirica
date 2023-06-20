v =float(input("valor de vendas"))
if(v<=1000):
	vendas = v*5/100
	print(round(vendas,2))
else:
	vendas = (1000*5/100)
	d = v-1000
	total = vendas+d*(10/100)
	
	print(round(total,2))