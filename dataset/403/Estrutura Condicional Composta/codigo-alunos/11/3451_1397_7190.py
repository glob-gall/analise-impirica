a = float(input("area: "))

if(a<=10000):
	vt = a * 5
	print(vt)
else:
	vb = a - 10000
	va = a - vb
	vt = (va*5)+(vb*4)
	print(vt)



