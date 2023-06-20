from numpy import *
x = array(eval(input("Vetor dos aneis acertadso por um jogador: ")))
p = 200

for i in range(0,size(x)):
	if x[i]==1:
		p = p*4
	elif x[i]==2:
		p = p*2
	elif x[i]==3:
		p = p*1
	elif x[i]==4:
		p = p/2
print(round(p,2))