nome = input().upper()
qnt = int(input())

if(qnt < 0 or qnt > 50):
	print("Entrada invalida")
	
elif(nome == "ARROZ"):
	g = qnt * 500
	print(g)
	
elif(nome == "CENOURA"):
	g = qnt * 100
	print(g)
	
elif(nome == "KAMPYO"):
	g = qnt * 20
	print(g)
	
elif(nome == "NORI"):
	g = qnt * 50
	print(g)
	
elif(nome == "OMELETE"):
	g = qnt * 200
	print(g)
	
elif(nome == "PEPINO"):
	g = qnt * 150
	print(g)
	
elif(nome == "SALMAO"):
	g = qnt * 300
	print(g)

elif(nome == "SHITAKE"):
	g = qnt * 150
	print(g)