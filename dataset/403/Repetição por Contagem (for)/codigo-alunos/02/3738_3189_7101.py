from numpy import*
v1 = array(eval(input("Media Final: ")))
v2 = array(eval(input("Numero de Horas: ")))
x = int(input("Carga horaria da disciplina: "))
y = zeros(3, dtype=int)
for i in range(0,size(v1)):
	if (v2[i]>=0.75*x and v1[i]>=5):
		y[0]=y[0]+1
	elif (v1[i]<5 and v2[i]>=0.75*x):
		y[1]=y[1]+1
	else:
		y[2]=y[2]+1
print(y)