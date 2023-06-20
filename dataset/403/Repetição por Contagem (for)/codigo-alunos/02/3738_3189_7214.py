from numpy import*
n = array(eval(input("Notas: ")))
f = array(eval(input("Frequencia: ")))
c = int(input("Cargo: "))

vcont = zeros(3, dtype=int)
for i in range (0, size(n)):
	if (n[i] >= 5) and (f[i] >= 0.75*c):
		vcont[0] = vcont[0]+1
	elif (n[i] < 5) and (f[i] >= 0.75*c):
		vcont[1] += 1
	else:
		vcont[2] += 1
print(vcont)