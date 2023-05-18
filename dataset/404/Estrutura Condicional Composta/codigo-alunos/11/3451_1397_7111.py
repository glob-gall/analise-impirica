a = float (input("Qual e a area a ser fertilizada?"))
vt = 5 * a
exc = a - 10000
vt2 = (5 * 10000) + (exc * 4 )

if (a <= 10000):
	print (round(vt,2))
else:
	print (round(vt2,2))