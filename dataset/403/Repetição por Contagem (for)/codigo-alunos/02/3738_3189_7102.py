from numpy import *

me = array(eval(input()))
fre = array(eval(input()))
ch = int(input())

v = zeros(3, dtype=int)

for i in range(0,size(fre)):
	
	if (fre[i] >= 0.75 * ch) and (me[i] >= 5):
		v[0] = v[0] + 1
		
	elif (fre[i] >= 0.75 * ch) and (me[i] < 5):
		v[1] = v[1] + 1
		
	else:
		v[2] = v[2] + 1
		
print(v)