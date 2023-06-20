from numpy import *
f = array(eval(input()))
kcal = array(eval(input()))
i=0
k = 0

		
while(i<size(kcal)):
	if(f[i] == "ARROZ"):
		k += 1.25*kcal[i]
	elif(f[i] == "FEIJAO"):
		k += 2.60*kcal[i]
	elif(f[i] == "BIS"):
		k += 1.80*kcal[i]
	elif(f[i] == "MIOJO"):
		k += 0.85*kcal[i]
	elif(f[i] == "FANTA"):
		k += 3.20*kcal[i]
	i+=1
	
print(round(k, 2))