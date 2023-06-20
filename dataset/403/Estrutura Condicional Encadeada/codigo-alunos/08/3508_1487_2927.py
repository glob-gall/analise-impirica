from math import*
N = input("Ingrediente: ").upper()
Q = int(input("Quantidade: "))

if (Q >= 0 and Q <=50):
	if N == "ARROZ":
		q = Q * 500
		print(q)
	elif(N == "CENOURA"):
		q = Q * 100
		print(q)
	elif(N == "KAMPYO"):
		q = Q * 20
		print(q)
	elif(N == "NORI"):
		q = Q * 50
		print(q)
	elif(N == "OMELETE"):
		q = Q * 200
		print(q)
	elif(N == "PEPINO"):
		q = Q * 150
		print(q)
	elif(N == "SALMAO"):
		q = Q * 300
		print(q)
	elif(N == "SHITAKE"):
		q = Q * 150
		print(q)
else:
	print("Entrada invalida")