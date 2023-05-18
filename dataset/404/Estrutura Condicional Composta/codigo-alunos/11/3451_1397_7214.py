a = float(input("Qual o tamanho da area: "))

if (a<=10000):
	v = 5.0 * a 
	print(round(v,2))
else:
	v = 5.0 * 10000
	vr = a - 10000
	vt = vr*4
	f = v + vt
	print(round(f,2))