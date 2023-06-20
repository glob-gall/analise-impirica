from numpy import *

n = array(eval(input()))
q = array(eval(input()))
j = ones(size(n),dtype=float)
i = 0

while(i<size(n)):
	if(n[i] == "ARROZ"):
		j[i]= 1.25
	if(n[i] == "FEIJAO"):
		j[i]=2.6
	if(n[i] == "BIS"):
		j[i]=1.8
	if(n[i] == "MIOJO"):
		j[i]=0.85
	if(n[i] == "FANTA"):
		j[i]=3.2
	i = i+1
x = j*q

print(round(sum(x),2))
