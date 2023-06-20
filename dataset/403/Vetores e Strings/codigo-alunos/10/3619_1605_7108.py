from numpy import*
vn= array(eval(input()))
p=200
i=0 
while i < size(vn):
	if vn[i]== 1:
		p= p*4
	elif vn[i]==2:
		p= p*2
	elif vn[i]==3:
		p=p
	else:
		p= p/2
	i= i+1
print(round(p,2))

	
	
	
	

