from numpy import * 
produtos = array(eval(input().upper()))
qdd = array(eval(input()))
i = 0
var = 0
while(i<size(produtos)):
	if(produtos[i]=="ARROZ"):
		var = var + 1.25*qdd[i]
		i = i +1
	elif(produtos[i]=="FEIJAO"):
		var = var + 2.60*qdd[i]
		i = i +1
	elif(produtos[i]=="BIS"):
		var = var + 1.80*qdd[i]
		i = i +1
	elif(produtos[i]=="MIOJO"):
		var = var + 0.85*qdd[i]
		i = i +1
	elif(produtos[i]=="FANTA"):
		var = var + 3.20*qdd[i]
		i = i +1
print(round(var,2))
