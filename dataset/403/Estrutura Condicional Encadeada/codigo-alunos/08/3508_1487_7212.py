n=input().upper()
q=int(input())

if(q>0 and q<50):
	if(n=="ARROZ"):
		i=q*500
		print(i)
	elif(n=="CENOURA"):
		i=q*100
		print(i)
	elif(n=="KAMPYO"):
		i=q*20
		print(i)
	elif(n=="NORI"):
		i=q*50
		print(i)
	elif(n=="OMELETE"):
		i=q*200
		print(i)
	elif(n=="PEPINO"):
		i=q*150
		print(i)
	elif(n=="SALMAO"):
		i=q*300
		print(i)
	elif(n=="SHITAKE"):
		i=q*150
		print(i)
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")