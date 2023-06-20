from numpy import *

# Vetor

vn = array(eval(input()))

# Variável Laço

cont = 0 # Progressao pelo vetor
soma = 200.0 # Total de pontos

while (cont < size(vn)):
	
	if (vn[cont] == 1):
		
		soma = soma * 4
		
	if (vn[cont] == 2):
		
		soma = soma * 2
		
	if (vn[cont] == 4):
		
		soma = soma/2
		
	
	cont = cont + 1

print (soma)