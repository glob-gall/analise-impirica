from numpy import *

a = array(eval(input())) # alimentos
q = array(eval(input())) # quantidades

cont = 0 # progressao pelos vetores
soma = 0 # quantidade de kcal

while (cont < size(a)):
	
	if (a[cont].upper() == 'ARROZ'):
		 
		 soma = soma + (q[cont] * 1.25)
		 
	elif (a[cont].upper() == 'FEIJAO'):
		 
		 soma = soma + (q[cont] * 2.60)
		 
	elif (a[cont].upper() == 'BIS'):
		 
		 soma = soma + (q[cont] * 1.80)
		 
	elif (a[cont].upper() == 'MIOJO'):
		 
		 soma = soma + (q[cont] * 0.85)
		 
	elif (a[cont].upper() == 'FANTA'):
		 
		 soma = soma + (q[cont] * 3.20)
		 
	
	cont = cont + 1

print (round(soma, 2))