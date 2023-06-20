from numpy import *
notas = array(eval(input()))
freq = array(eval(input()))
carga = int(input())

vcont = zeros(3,dtype = int)

for i in range(0, size(notas)):
	if(notas[i] >= 5) and (freq[i] >= 0.75*carga):
		vcont[0] = vcont[0] + 1
	elif (notas[i]<5) and (freq[i] >= 0.75*carga):
		vcont[1] = vcont[1] + 1
	else: 
		vcont[2] = vcont[2] + 1
print(vcont)