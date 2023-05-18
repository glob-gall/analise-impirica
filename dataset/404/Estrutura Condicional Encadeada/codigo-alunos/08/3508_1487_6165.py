ingredientes = input("Digite o nome do ingrediente: ")
quantidade = int(input("Digite a quantidade de receitas: "))
nome = ingredientes.upper()

if((0 < quantidade < 50) and (nome == "ARROZ" or nome == "CENOURA" or nome == "KAMPYO" or nome == "NORI" or nome == "OMELETE" or nome == "PEPINO" or nome == "SALMAO" or nome == "SHITAKE")):
	if(nome == "ARROZ"):
		valor = 500 * quantidade
		print(valor)
	elif(nome == "CENOURA"):
		valor = 100 * quantidade
		print(valor)
	elif(nome == "KAMPYO"):
		valor = 20 * quantidade
		print(valor)
	elif(nome == "NORI"):
		valor = 50 * quantidade
		print(valor)
	elif(nome == "OMELETE"):
		valor = 200 * quantidade
		print(valor)
	elif(nome == "PEPINO"):
		valor = 150 * quantidade
		print(valor)
	elif(nome == "SALMAO"):
		valor = 300 * quantidade
		print(valor)
	elif(nome == "SHIRAKE"):
		valor = 150 * quantidade
		print(valor)
else:
	print("Entrada invalida")
		