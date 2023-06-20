v= float(input())

if(v<=1000):
	print(round(v*0.05,2))
	
else:
	vendas=1000*0.05+((v-1000)*0.10)
	print(round(vendas,2))