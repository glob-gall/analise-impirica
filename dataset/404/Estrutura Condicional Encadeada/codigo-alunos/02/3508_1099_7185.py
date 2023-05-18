# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import *

a = float(input ("Lado a: "))
b = float(input ("Lado b: "))
c = float(input ("Lado c: "))

print("Entradas:", a, ",", b, ",", c)

if (a > 0 and b > 0 and c > 0):
	if (a < b + c and b < c + a and c < b + a):
		if (a == b and b == c):
			print ("Tipo de triangulo: equilatero")
		elif (a == b or b == c or c == a):
			print ("Tipo de triangulo: isosceles")
		else:
			print ("Tipo de triangulo: escaleno")
	else:
		print ("Tipo de triangulo: invalido")
else:
	print ("Tipo de triangulo: invalido")