#a área a ser fertilizada (em hectares).
area = float(input("area a ser fertilizada: "))
if (area > 10000):
	t = 5 * 10000 + (area - 10000)*4
	print(t)
else:
	f = area * 5
	print(f)