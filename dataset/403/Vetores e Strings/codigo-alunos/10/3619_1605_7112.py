from numpy import*

v = array(eval(input()))
p = 200
for i in range(0, size(v)):
	if (v[i]== 1):
		p = p*4
	if(v[i] == 2):
		p = p *2
	if (v[i]==3):
		p = p
	if(v[i] == 4):
		p = p/2
		
print(round(p, 2))