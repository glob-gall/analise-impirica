#total
from numpy import*

item= array(eval(input().upper()))
qt=array(eval(input()))

i=0
total=0

while(i<size(item)):
	if (item[i]=="ARROZ"):
		total= total + qt[i]*1.25
	elif (item[i]=="FEIJAO"):
		total= total + qt[i]*2.6
	elif (item[i]=="BIS"):
		total= total + qt[i]*1.8
	elif (item[i]=="MIOJO"):
		total= total + qt[i]*0.85
	elif (item[i]=="FANTA"):
		total= total + qt[i]*3.2
	i= i+1
print(round(total,2))
