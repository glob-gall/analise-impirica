# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *

ladoA = float(input("Digite o lado A do triangulo, "))
ladoB = float(input("Digite o lado B do triangulo, "))
ladoC = float(input("Digite o lado C do triangulo, "))

s = (ladoA+ladoB+ladoC)/2
x = s*(s-ladoA)*(s-ladoB)*(s-ladoC)
area = sqrt(x)

print(round(area, 5))


