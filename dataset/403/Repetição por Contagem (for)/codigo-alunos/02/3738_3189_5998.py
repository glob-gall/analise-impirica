from numpy import *
m = array(eval(input("Vetor de medias: ")))
f = array(eval(input("Vetor de frequecia: ")))
h = int(input("Carga Horaria: "))

v = zeros(3, dtype=int)
for i in range(0,size(f)):
	if (f[i]>=0.75*h) and (m[i]>=5):
		v[0]=v[0]+1
	elif (f[i]>=0.75*h) and (m[i]<5):
		v[1]=v[1]+1
	else:
		v[2]=v[2]+1
print(v)