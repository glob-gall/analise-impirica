from math import*
a = float(input())
b = float(input())
c = float(input())

print("Entradas: ", a,",",b,",",c)

if(a>0 and b > 0 and c>0):
	if(a+b>c and a+c>b and c+b>a):	
		if(a == b and b==c):
			print("Tipo de triangulo: equilatero")
		if(a == b or b == c or a == c):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
	else:
		print("Tipo de triangulo: invalido")
else:
		print("Tipo de triangulo: invalido")


