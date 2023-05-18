c1 = int(input("digite o numero de votos do candidato mais votado: "))
c2 = int(input("digite o numero de votos do segundo candidato mais votado: "))
c3 =  int(input("digite o numero de votos do candidadto menos votado: "))
metade = (c1+c2+c3)/2
if(c1 <= metade):	
	print("SIM")
else:	
	print("NAO")