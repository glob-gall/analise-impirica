from numpy import*
mf= array(eval(input()))
pres= array(eval(input()))
ch= int(input())

cont= zeros(3, dtype=int)
for h in range(0,size(mf)):
	if(mf[h] >= 5) and (pres[h] >= 0.75*ch):
		cont[0] = cont[0]+1
	elif(mf[h] < 5) and (pres[h] >= 0.75*ch):
		cont[1]= cont[1] + 1
	else:
		cont[2] = cont[2] + 1
print(cont)
	
