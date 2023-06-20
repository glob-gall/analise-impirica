# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

from math import*

A = float(input ("Lado 1: "))
B = float(input ("Lado 2: "))
C = float(input ("Lado 3: "))

print("Entradas:", A, ",", B, ",", C)
if (A>0 and B>0 and C>0) and (A<B+C and B<A+C and C<A+B): 
	if(A==B and B==C and A==C):
		print("Tipo de triangulo: equilatero")
	elif(A == B and A !=C) or (A == C and A != B) or (B == C and B != A):
		print("Tipo de triangulo: isosceles ")
	else:		
		print("Tipo de triangulo: escaleno")
else:
		print("Tipo de triangulo: invalido")
	
	
