# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a= float(input("lado1"))
b= float(input("lado2"))
c= float(input("lado3"))

print("Entradas:", a,",",b, ",",c)
if (a>0)and (b>0)and (a>0):
	if(a< b+c)and(b< a+c)and(c< a+b):
		if (a==b)and(b==c):
			print("Tipo de triangulo: equilatero")
		elif (a==b)or(b==c)or(c==a):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")