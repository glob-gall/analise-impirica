vv= float(input())

if(vv<=1000):
	print(round(vv*0.05,2))
else: 
	vendas= 1000*0.05+((vv-1000)*0.1)
	
	print(round(vendas,2))