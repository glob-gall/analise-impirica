a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

print("Entradas:", a ,",", b , ",", c)

if (a > 0 and b > 0 and c > 0):
	if (a + b > c and a + c > b and b + c > a):
		if (a == b == c):
			print("Tipo de triangulo: equilatero")
		elif (a == b or a == c or b == c):
			print("Tipo de triangulo: isosceles")
		elif (a != b != c):
			print("Tipo de triangulo: escaleno")
		else:
		 	print("Tipo de triangulo: invalido")
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")