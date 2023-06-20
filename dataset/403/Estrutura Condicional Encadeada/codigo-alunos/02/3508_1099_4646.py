# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import*
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
print("Entradas:", a, ",", b, ",", c)
if (a > 0  and b>0 and c>0):
	if(c<a+b and b<a+c and a<b+c):
		if(a==b and b==c and a==c):
			print("Tipo de triangulo: equilatero ")
		elif((a==b) and (c!=a) or (b==c) and (a!=c)):
			print("Tipo de triangulo: isosceles ")
		else:
			print("Tipo de triangulo: escaleno ")
	else:
		print("Tipo de triangulo: invalido ")
else:
	print("Tipo de triangulo: invalido ")