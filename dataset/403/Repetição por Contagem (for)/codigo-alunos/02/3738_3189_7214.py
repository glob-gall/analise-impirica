from numpy import*
n = array(eval(input()))
f = array(eval(input()))
c = int(input())

vcont = zeros(3, dtype=int)
for i in range (0, size(n)):
	if (n[i] >= 5) and (f[i] >= 0.75*c):
		vcont[0] = vcont[0]+1
	elif (n[i] < 5) and (f[i] >= 0.75*c):
		vcont[1] += 1
	else:
		vcont[2] += 1
print(vcont)
