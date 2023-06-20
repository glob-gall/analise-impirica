from numpy import*
v = array(eval(input()))

i = 0
p = 200.0

while i< size(v):
	if v[i] == 1:
		p = p*4
		
	elif v[i] == 2:
		p = p*2
		
	elif v[i] == 3:
		p = p
		
	elif v[i] == 4:
		p = p/2
		
	i = i + 1
	
print(round(p, 2))