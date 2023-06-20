from numpy import*
v1 = array(eval(input()))
v2 = array(eval(input()))
i = 0
j = 0
while (i<size(v2)):
	if (v1[i]=="ARROZ"):
		j = j + (v2[i] * 1.25)
	elif (v1[i]=="FEIJAO"):
		j = j + (v2[i] * 2.60)
	elif (v1[i]=="BIS"):
		j = j + (v2[i] * 1.80)
	elif (v1[i]=="MIOJO"):
		j = j + (v2[i] * 0.85)
	elif (v1[i]=="FANTA"):
		j = j + (v2[i] * 3.20)
	i = i + 1
print(round(j,2))
