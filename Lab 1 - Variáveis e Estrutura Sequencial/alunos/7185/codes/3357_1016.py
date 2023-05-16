# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *
a = float(input("digite o comprimento do lado A de um triangulo: "))
b = float(input("digite o comprimento do lado B de um triangulo: "))
c = float(input("digite o comprimento do lado C de um triangulo: "))
s = (a + b + c) / 2
area = sqrt(s * (s-a)*(s-b)*(s-c))
print (round(area, 5))