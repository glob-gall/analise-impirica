v = float(input("valor: "))

c = 0.05 * v

if(v<=1000):
	print(round(c,2))
else:
	d = v - 1000
	b = d * 0.10 + 1000 * 0.05
	print(round(b,2))



