n = input("Ingrediente: ").upper()
q = int(input("Quantidade de receitas: "))
if q>=0 and q<=50:
	if n == "ARROZ":
		a = 500 * q
		print(a)
	elif n == "CENOURA":
	   b = 100*q
	   print(b)
	elif n == "KAMPYO":
	   c = 20*q
	   print(c)
	elif n == "NORI":
	   d = 50 *q
	   print(d)
	elif n == "OMELETE":
	   e = 200*q
	   print(e)
	elif n == "PEPINO":
		f = 150*q
		print(f)
	elif n == "SALMAO":
		g = 300*q
		print(g)
	else:
		h = 150*q
		print(h)
else:
	print("Entrada invalida")
	
	
	