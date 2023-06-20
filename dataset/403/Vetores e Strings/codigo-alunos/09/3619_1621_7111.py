from numpy import*
p= array(eval(input().upper()))
q= array(eval(input()))

i=0
v=0
while (i<size(p)):
	if (p[i]=="ARROZ"):
		v= v +(q[i]*1.25)
	if (p[i]=="FEIJAO"):
		v= v +(q[i]*2.60)
	if (p[i]=="BIS"):
		v=v +(q[i]* 1.80)
	if (p[i]=="MIOJO"):
		v= v+(q[i]*0.85)
	if (p[i]=="FANTA"):
		v= v +(q[i]* 3.20)
	i=i+1
	total= sum(v)
print(round(total,2))
