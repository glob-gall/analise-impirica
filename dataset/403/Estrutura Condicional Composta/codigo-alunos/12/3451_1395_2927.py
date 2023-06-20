vl= float(input("venda: "))

if(vl<=1000):
	venda= (vl*5/100)
	print(round(venda,2))
else:
	venda=(1000*5/100)
	c= vl-1000
	total=venda+c*(10/100)
	print(round(total,2))
