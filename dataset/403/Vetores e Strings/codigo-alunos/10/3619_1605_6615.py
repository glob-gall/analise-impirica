from numpy import*
vet = array(eval(input("aneis acertados: ")))
i = 0
pontos = 200.0
while(i<size(vet)):
	if(vet[i]==1):
		pontos = pontos * 4
		i = i + 1
	elif(vet[i]==2):
		pontos = pontos * 2
		i = i + 1
	elif(vet[i]==3):
		pontos = pontos
		i = i + 1
	elif(vet[i]==4):
		pontos = pontos/2
		i = i + 1
print(round(pontos,2))