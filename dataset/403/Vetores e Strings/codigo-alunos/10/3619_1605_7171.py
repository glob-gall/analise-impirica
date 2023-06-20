#tiro ao alvo
from numpy import*

alvo= array(eval(input("Digite o vetor de alvos:")))

i=0
pts=200
#total=0

while (i<size(alvo)):
	if (alvo[i]==1):
		pts= pts*4
	elif (alvo[i]==2):
		pts= pts*2
	elif (alvo[i]==3):
		pts= pts 
	elif (alvo[i]==4):
		pts=(pts/2)
	i= i+1
print(round(pts,2))

	
