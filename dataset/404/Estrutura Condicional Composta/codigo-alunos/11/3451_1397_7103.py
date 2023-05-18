area = float(input())

if	area<=10000:
	valor = 5 * area
	print(round(valor,2))
else:
	t = area-10000
	valor = (5 *10000) + (4*t)
	print(round(valor,2))