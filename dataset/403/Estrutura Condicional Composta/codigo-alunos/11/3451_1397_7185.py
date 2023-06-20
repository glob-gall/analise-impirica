area = float(input("Digite a area a ser fertilizada (em hectares): "))
if (area <= 10000):
	vt = (area * 5)
	print(round(vt, 2))
else:
	area1 = (area - 10000)
	vt = (10000 * 5) + (area1 * 4)
	print(round(vt, 2))
