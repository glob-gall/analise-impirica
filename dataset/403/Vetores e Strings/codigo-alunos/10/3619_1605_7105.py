from numpy import *
n = array(eval(input()))
i = 0
soma = 200

while(i<size(n)):
	if(n[i] == 1):
		soma = soma*4
	elif(n[i] == 2):
		soma = soma*2
	elif(n[i] == 4):
		soma = soma/2
	i +=1
print(round(soma,2))