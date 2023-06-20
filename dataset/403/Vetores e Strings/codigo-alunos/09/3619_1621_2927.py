from numpy import * 

v= array(eval(input()))
v1=array(eval(input()))
i=0
j=0
while(i<size(v)):
	if(v[i]=="ARROZ"):
		j= j + (1.25 * v1[i])
	elif(v[i]=="FEIJAO"):
		j= j + (2.60 * v1[i])
	elif(v[i]=="BIS"):
		j= j + (1.80 * v1[i])
	elif(v[i]=="MIOJO"):
		j= j + (0.85 * v1[i])
	elif(v[i]=="FANTA"):
		j= j + (3.20 * v1[i])
	i= i +1
print(round(j,2))




