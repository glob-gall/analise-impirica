nome = input("Nome do ingrediente: ").upper()
qnt = int(input("Quantidade de receitas: "))
if (0<=qnt<=50):
	if (nome=="ARROZ"):
		x=qnt*500
		print(x)
	elif (nome=="CENOURA"):
		x=qnt*100
		print(x)
	elif (nome=="KAMPYO"):
		x=qnt*20
		print(x)
	elif (nome=="NORI"):
		x=qnt*50
		print(x)
	elif (nome=="OMELETE"):
		x=qnt*200
		print(x)
	elif (nome=="PEPINO"):
		x=qnt*150
		print(x)
	elif (nome=="SALMAO"):
		x=qnt*300
		print(x)
	elif (nome=="SHITAKE"):
		x=qnt*150
		print(x)
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")