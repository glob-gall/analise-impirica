from numpy import*
v=array(eval(input("pontos:")))
i=0
p=200
while(i<size(v)):
	if(v[i]==1):
		p=p*4
		i=i+1
	elif(v[i]==2):
		p=p*2
		i=i+1
	elif(v[i]==3):
		p=p
		i=i+1
	elif(v[i]==4):
		p=p/2
		i=i+1
print(round(p,2))