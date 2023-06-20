from numpy import *

v = array(eval(input(":")))
v1 = ones(size(v),dtype=int)
i = 0
p = 200
while(i<size(v)):
	if(v[i]==1):
		p=p*4
	if(v[i]==2):
		p=p*2
	if(v[i]==4):
		p=p/2
	i = i+1
	
print(round(sum(p),2))



