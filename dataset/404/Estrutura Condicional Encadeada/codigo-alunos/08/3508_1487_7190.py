n = input("nome:").upper()
q = int(input("quantidade:"))

if(0<q<50):
	if(n=="ARROZ"):
		print(q*500)
	elif(n=="CENOURA"):
		print(q*100)
	elif(n=="KAMPYO"):
		print(q*20)
	elif(n=="NORI"):
	   print(q*50)
	elif(n=="OMELETE"):
	   print(q*200)
	elif(n=="PEPINO"):
	   print(q*150)
	elif(n=="SALMAO"):
	   print(q*300)
	elif(n=="SHITAKE"):
	   print(q*150)
	else:
	   print("Entrada invalida")
else:
	print("Entrada invalida")


	



