from numpy import *
a = array(eval(input()))
b = array(eval(input()))
c = int(input())
n = zeros(3, dtype = int)

for i in range (0, size(b)):
	if (b[i]>=0.75* c) and (a[i]>=5):
		n[0] = n[0] + 1 
	elif (b[i] >=0.75 * c) and (a[i]<5):
		n[1] = n[1] + 1
	else:
		n[2] = n[2] + 1
print(n)
