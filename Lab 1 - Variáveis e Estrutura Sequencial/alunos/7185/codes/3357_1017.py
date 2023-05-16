# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *
r = 6371.01
t1 = radians(float(input("Digite a latitude de P1: ")))
g1 = radians(float(input("Digite a longitude de P1: ")))
t2 = radians(float(input("Digite a latitude de P2: ")))
g2 = radians(float(input("Digite a longitude de P2: ")))
d= r * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * (cos(g1 - g2)))
print (round(d, 2))

-3.130601
-60.02306
-3.083550
-60.027781