#sushi
ing= input("Digite o ingrediente:").upper()
rec= int(input("Para quantas receitas?"))

if (rec>0) and (rec<50):
	if (ing=="ARROZ"):
		qnt= rec *500
		print(qnt)
	elif (ing=="CENOURA"):
		qnt= rec*100
		print(qnt)
	elif (ing=="KAMPYO"):
		qnt= rec*20
		print(qnt)
	elif (ing=="NORI"):
		qnt= rec*50
		print(qnt)
	elif (ing=="OMELETE"):
		qnt= rec*200
		print(qnt)
	elif (ing=="PEPINO"):
		qnt= rec*150
		print(qnt)
	elif (ing=="SALMAO"):
		qnt= rec*300
		print(qnt)
	elif (ing=="SHITAKE"):
		qnt=rec*150
		print(qnt)
else:
	print("Entrada invalida")


	