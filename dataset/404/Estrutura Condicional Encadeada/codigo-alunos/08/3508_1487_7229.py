n=input().upper()
q=int(input())

if(q>0 and q<50):
	if(n=="ARROZ"):
		v=q*500
		print(v)
	elif(n=="CENOURA"):
		v=q*100
		print(v)
	elif(n=="KAMPYO"):
		v=q*20
		print(v)
	elif(n=="NORI"):
		v=q*50
		print(v)
	elif(n=="OMELETE"):
		v=q*200
		print(v)
	elif(n=="PEPINO"):
		v=q*150
		print(v)
	elif(n=="SALMAO"):
		v=q*300
		print(v)
	elif(n=="SHITAKE"):
		v=q*150
		print(v)
else:
	print("Entrada invalida")