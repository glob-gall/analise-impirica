#Nome
n = input("Nome do ingediente: ").upper()
#quantidade de receitas
qr = int(input("Quantas receitas? "))

if (0<=qr<=50):
	if (n=="ARROZ"):
		qg = 500
	elif (n=="CENOURA"):
		qg = 100
	elif (n=="KAMPYO"):
		qg = 20
	elif (n=="NORI"):
		qg = 50
	elif (n=="OMELETE"):
		qg = 200
	elif (n=="PEPINO"):
		qg = 150
	elif (n=="SALMAO"):
		qg = 300
	elif (n=="SHITAKE"):
		qg = 150
	print(qg*qr)
else:
	print('Entrada invalida')