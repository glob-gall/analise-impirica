from math import *

a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se todas as entradas são positivas
if (a>=0)and(b>=0)and(c>=0):
	# Testa se medidas correspondem aas de um triangulo
	if (a< b+c)and(b< a+c)and(c< a+b):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		area = round(area, 3)
		print("Area:", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
