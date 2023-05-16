# Teste seu codigo aos poucos.
from math import *
a = float(input(" Comprimento do lado a : "))
b = float(input(" Comprimento do lado b : "))
c = float(input(" Comprimento do lado c : "))
sem = (a + b + c)/ 2
area = sqrt(sem * ( sem - a ) * (sem - b) * (sem - c))
print(round(area,5))
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
