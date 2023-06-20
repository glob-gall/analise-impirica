from numpy import*

vn= array(eval(input("vetor de numeros aneis:")))
pi= 200.0
i=0

while (i<size(vn)):
	if (vn[i]== 1):
		pi= pi*4
	if (vn[i]== 2):
		pi= pi*2
	if (vn[i]== 3):
		pi= pi
	if (vn[i]== 4):
		pi= pi/2
	i=i+1
	pt= sum(pi)
print(round(pt,2))