v= float(input("valor: "))

if(v<=1000):
	c = 0.05 * v
	print(round(c,2))
	
else:
	p = v-1000
	c = (1000 * 0.05)+(p * 0.10)
	print(round(c,2))




