n = input("nome do ingrediente:  ").upper()
q = int(input("Quantidade de ingredientes:  "))

if (q>=0 and q<=50):
	if n== "ARROZ":
		qi =500
		
	elif n == "CENOURA":
		qi = 100
		
	elif n == "KAMPYO":
		qi = 20
		
	elif n == "NORI":
		qi = 50
		
	elif n == "PEPINO":
		qi = 150
		
	elif n == "SALMAO":
		qi = 300
		
	elif n == "SHITAKE":
		qi = 150
		
	print(q*qi)
	
else:
	print("Entrada invalida")