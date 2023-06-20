from numpy import*
vn= array(eval(input("vetor de numeros")))
pts=200
i=0 
while i < size(vn):
	if vn[i]== 1:
		pts= pts * 4
	elif vn[i]== 2:
		pts= pts * 2
	elif vn[i]==3:
		pts=pts
	elif vn[i]==4:
		pts= pts/2
	i= i+1
	
print(round(pts,2))