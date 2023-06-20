la=float(input())
lb=float(input())
lc=float(input())

print("Entradas:", la, ",", lb, ",", lc)

if(la>0 and lb>0 and lc>0):
	if(la<lc+lb and lb<la+lc and lc<la+lb):
		if(la==lb and lb==lc and la==lc):
			print("Tipo de triangulo: equilatero")
		elif(la==lb or lb==lc or lc==la):
				print("Tipo de triangulo: isosceles")
		else:
				print("Tipo de triangulo: escaleno")
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")
	