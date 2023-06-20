from numpy import*

ar = array(eval(input()))
pi = 200

cont1 = 0


while(cont1 < size(ar)):
	
	if(ar[cont1] == 1):
		pi = pi * 4
		
	elif(ar[cont1] == 2):
		pi = pi * 2
		
	elif(ar[cont1] == 3):
		pi = pi
	
	elif(ar[cont1] == 4):
		pi = pi / 2
		
	cont1 = cont1 + 1
		
print(pi)

