# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import *

a = float(input("De um valor ao lado a: "))
b = float(input("De um valor ao lado b: "))
c = float(input("De um valor ao lado c: "))

print("Entradas:",a,",",b,",",c)

if (((b+c) > a) and ((a+c) > b) and ((a+b) > c)):
   if(a == b and b == c and c == b):
      a = "equilatero"
      print("Tipo de triangulo:",a)
   elif(a == b or b == c or c == a):
      b = "isosceles"
      print("Tipo de triangulo:",b)
   elif(a != b or a != c or b != c):
      c = "escaleno"
      print("Tipo de triangulo:", c) 
else:
   d = "invalido"
   print("Tipo de triangulo:", d)