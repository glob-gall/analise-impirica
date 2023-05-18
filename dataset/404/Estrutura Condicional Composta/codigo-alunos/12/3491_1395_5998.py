v = float(input("vendas: "))

if v <= 1000:
	c = 0.05*v
else:
	x = v-1000
	c = 0.05*1000 + x*0.1
	
print(round(c,2))