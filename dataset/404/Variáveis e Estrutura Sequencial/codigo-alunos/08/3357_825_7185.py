# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *
raio = float(input("Digite o valor de um raio r: "))
areac = (raio**2) * pi
vol_e = ((raio**3) * pi) * 4 /  3
print (round (areac, 3))
print (round(vol_e, 3))