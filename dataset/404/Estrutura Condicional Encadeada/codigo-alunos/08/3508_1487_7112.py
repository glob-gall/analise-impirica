N = input("Nome: ").upper()
Q = int(input("Quantidade: "))

if( Q <=0 or Q > 50):
	q = "Entrada invalida"
else: 
	if( N == "ARROZ"):
		q = Q*500
	elif( N == "CENOURA"):
		q = Q*100
	elif( N == "KAMPYO"):
		q = Q*20
	elif( N == "NORI"):
		q = Q*50
	elif( N == "OMELETE"):
		q = Q*200
	elif( N == "PEPINO"):
		q = Q*150
	elif( N == "SALMAO"):
		q = Q*300
	elif( N == "SHITAKE"):
		q = Q*150
	else:
		q = "Entrada invalida"



	
print(q)