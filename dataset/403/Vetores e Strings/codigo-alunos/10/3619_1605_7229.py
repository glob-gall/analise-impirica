from numpy import*

a = array(eval(input()))
pi = 200

c1 = 0

while(c1 < size(a)):
	
	if(a[c1] == 1):
		pi = pi * 4
	elif(a[c1] == 2):
		pi = pi * 2
	elif(a[c1] == 3):
		pi = pi
	elif(a[c1] == 4):
		pi = pi / 2
		
	c1 = c1 + 1
		
print(pi)