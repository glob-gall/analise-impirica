from numpy import *

a = array(eval(input()))
pi = 200

i = 0


while(i < size(a)):
	
	if(a[i] == 1):
		pi = pi * 4
		
	elif(a[i] == 2):
		pi = pi * 2
		
	elif(a[i] == 3):
		pi = pi
	
	elif(a[i] == 4):
		pi = pi / 2
		
	i = i + 1
		
print(pi)