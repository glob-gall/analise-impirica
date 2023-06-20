from numpy import*

x = array(eval(input("aneis: ")))
p = 200
i = 0

while i<size(x):
	if x[i]==1:
	   p=p*4
	if x[i]==2:
	   p=p*2
	if x[i]==3:
	   p=p
	if x[i]==4:
	   p=p/2
	i+=1
	
print(round(p,2))