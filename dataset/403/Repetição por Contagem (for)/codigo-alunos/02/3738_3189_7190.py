from numpy import *

v = array(eval(input()))
f = array(eval(input()))
c = int(input())
v1 = zeros(3,dtype=int)

a = c*75/100
i = 0
A = 0
N = 0
F = 0


for i in range(size(v)):
	if(v[i]<5):
		N = N + 1
	if(f[i]<a):
		F = F + 1
	if(v[i]>=5 and f[i]>=a):
		A = A + 1
	i = i+1
	
v1[0] = A
v1[1] = N
v1[2] = F

print(v1)
	
