from numpy import*

pr = array(eval(input().upper()))
qu = array(eval(input()))
i = 0
v = zeros(size(qu))
while i<size(pr):
	if pr[i]=="ARROZ":
	   v[i]=1.25
	if pr[i]=="FEIJAO":
	   v[i]=2.60
	if pr[i]=="BIS":
	   v[i]=1.80
	if pr[i]=="MIOJO":
	   v[i]=0.85
	if pr[i]=="FANTA":
	   v[i]=3.20
	i+=1
a = sum(v*qu)
print(round(a,2))
