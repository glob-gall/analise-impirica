from numpy import *

u = array(eval(input()))
v = array(eval(input()))

d = 0

for i in range(0,size(v)):
	if u[i]=="ARROZ":
		d = (1.25 * v[i])+ d
	elif u[i]=="FEIJAO":
		d = (2.60* v[i]) + d
	elif u[i]=="BIS":
		d = (1.80*v[i]) + d
	elif u[i]=="MIOJO":
		d = (0.85*v[i]) + d
	elif u[i]=="FANTA":
		d = (3.20*v[i]) + d
print(round(d,2))