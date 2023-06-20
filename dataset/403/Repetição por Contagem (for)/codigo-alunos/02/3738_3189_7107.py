from numpy import *

vnf = array(eval(input()))
vp = array(eval(input()))
ch = int(input())
c = 0
c2 = 0 
c3 = 0
f = ch * (75/100)
vv = []

for i in range(size(vnf)):
	
	if(vp[i] >= f):
		
		if(vnf[i] >= 5):
			c = c + 1
			
		else:
			c2 = c2 + 1
			
	else:
		c3 = c3 + 1

vv.append(c)
vv.append(c2)
vv.append(c3)

vv = array(vv)
print(vv)