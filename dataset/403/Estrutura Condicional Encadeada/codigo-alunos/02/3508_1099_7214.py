# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

print("Entradas:", a , ",", b , "," , c)

if a<(b + c) and b<(a + c) and c<(a + b):
	if (a==b) and (b==c):
		t = "equilatero"
	elif ((a==b) or (a==c) or (b==c)):
		t = 'isosceles'
	else:
		t = 'escaleno'
else:
	t = "invalido"
	
print("Tipo de triangulo:", t )