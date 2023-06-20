from numpy import*
jogadas = array(eval(input("Pontuacao: ")))

i = 0 
ponto = 200 


while i<size(jogadas):
	if jogadas[i]==1:
		ponto =  ponto * 4 
	elif jogadas[i] == 2:
		ponto = ponto *2 
	elif jogadas[i] == 4:
		ponto = ponto/2 
	
	i = i + 1

print(round(ponto,2))