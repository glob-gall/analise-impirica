#notas
from numpy import*

mf=array(eval(input("Digite o vetor de medias:")))
fq=array(eval(input("Digite o vetor da frequencia:")))
ch=float(input("Digite a carga horaria:"))

vet= zeros(3,dtype=int)
fqmin= (ch * 0.75)

ap=0 #aprovado
rpn=0 #rep. notas
rpf=0 #rep. frequência

for i in range(size(mf)):
	if (mf[i]>=5) and (fq[i]>=fqmin):
		ap=ap+1
		vet[0]=ap
	elif(mf[i]<5):
		rpn= rpn+1
		vet[1]=rpn
	elif(fq[i]<fqmin):
		rpf= rpf+1
		vet[2]=rpf
print(vet)
	
	
					