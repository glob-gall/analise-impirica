h = float(input("hactares"))
if(h<=10000):
	custo = h*5 
	print(round(custo,2))
else:
	d = h-10000
	total = 50000+d*4
	print(round(total,2))