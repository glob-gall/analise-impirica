a = float(input("Lado A:"))
b = float(input("Lado B:"))
c = float(input("Lado C:"))

print("Entradas:", a,",",b,",",c)

if ((a>0) and (b>0) and (c>0)):
	if((a<b+c) and (b<a+c) and (c<a+b)):
		if((a==b) and (b==c)):
			tipo = "equilatero"
		elif ((a==b) or (b==c)):
			tipo = "isosceles"
		else:
			tipo = "escaleno"
		print("Tipo de triangulo:",tipo)			
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")
	
