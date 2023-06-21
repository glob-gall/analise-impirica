from numpy import * 
M = array(eval(input()))
h = array(eval(input()))
Ch = int(input())

ap = 0
rp = 0
rpf = 0
j = zeros(3, dtype=int)
for i in range(size(M)):
	if((M[i]>=5.0)and(h[i]>=(Ch*0.75))):
		ap = ap +1
		j[0]= ap
	elif((M[i]<5.0))and(h[i]>=(Ch*0.75)):
		rp = rp + 1
		j[1]=rp
	elif(h[i]<(Ch*0.75)):
		rpf = rpf + 1
		j[2]=rpf
print(j)
