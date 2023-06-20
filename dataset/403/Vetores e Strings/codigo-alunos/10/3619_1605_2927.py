from numpy import *

v= array(eval(input("VETOR DE NUMEROS: ")))

i= 0
j = 200.0

while( i < size(v)):
	if(v[i]==1):
		j= j * 4
	elif(v[i]==2):
		j= j  * 2	
	elif(v[i]==3):
		j= j 
	elif(v[i]==4):
		j= j / 2
	i = i + 1	
	
print(round(j,2))
