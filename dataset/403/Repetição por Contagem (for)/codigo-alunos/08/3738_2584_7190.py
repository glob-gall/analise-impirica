from numpy import *

n = int(input(":"))

c = 2
k = 3
x = 1-(1/2)
y = 1/k
while(c<n-1):
	c=c+2
	x = x - 1/c
while(k<n-1):
	k = k+2
	y = y + 1/k
if(n == 1):
	print("H =",1)
elif(n == 2):
	print("H =",round(1-1/2,6))

else:
	print("H =",round(x+y,6))
	

	
	
	



