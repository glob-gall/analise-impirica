a = float(input("Digite a area a ser fertilizada: "))
if a <= 10000:
	m1 = a * 5.0
	print(round(m1,2))
else:
	e = a - 10000
	b = a - e
	m2 = (b * 5.00) + (e * 4.00)
	print(round(m2,2))