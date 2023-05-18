ni= input("nome do ingrediente").upper()
qr= int(input("quantidade da receita"))
if 0<qr<50:
	if ni== "ARROZ" or "CENOURA" or "KAMPYO" or "NORI"or"OMELETE"or"PEPINO"or"SALMAO"or"SHITAKE":
		if ni=="ARROZ":	
			qni= qr * 500
			print(qni)
		elif ni=="CENOURA":
			qni= qr * 100
			print(qni)
		elif ni=="KAMPYO":
			qni= qr * 20
			print(qni)
		elif ni=="NORI":
			qni= qr * 50
			print(qni)
		elif ni=="OMELETE":
			qni= qr * 200
			print(qni)
		elif ni=="PEPINO":
			qni= qr * 150
			print(qni)
		elif ni=="SALMAO":
			qni= qr * 300
			print(qni)
		elif ni=="SHITAKE":
			qni= qr * 150
			print(qni)
else:
	print("Entrada invalida")
		