from numpy import*

v = array(eval(input().upper()))
q = array(eval(input()))

i = 0
u = 0

while(i < size(q)):
		if(v[i] == "ARROZ"):
			u = u + q[i]*1.25
		elif(v[i] == "FEIJAO"):
			u = u + q[i]*2.60
		elif(v[i] == "BIS"):
			u = u + q[i]*1.80
		elif(v[i] == "MIOJO"):
			u = u + q[i]*0.85
		elif(v[i] == "FANTA"):
			u = u + q[i]*3.20
		i = i + 1
print(round(u, 2))
