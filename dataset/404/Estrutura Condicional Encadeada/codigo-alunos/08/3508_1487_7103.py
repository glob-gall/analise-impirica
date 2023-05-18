i = input().upper()
q = int(input())

if q>0 and q<=50:
	if	i=="ARROZ":
		a=500
		t = a * q
		print(t)
	elif i=="CENOURA":
		a=100
		t = a * q
		print(t)
	elif i=="KAMPYO":
		a=20
		t = a * q
		print(t)
	elif i=="NORI":
		a=50
		t = a * q
		print(t)
	elif i=="OMELETE":
		a=200
		t = a * q
		print(t)
	elif i=="PEPINO":
		a=150
		t = a * q
		print(t)
	elif i=="SALMAO":
		a=300
		t = a * q
		print(t)
	elif i=="SHITAKE":
		a=150
		t = a * q
		print(t)
else:
	print("Entrada invalida")



