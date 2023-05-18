# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *

r = 6371.01

lt1 = radians(float(input()))
lg1 = radians(float(input()))
lt2 = radians(float(input()))
lg2 = radians(float(input()))

d = r * acos(sin(lt1)*sin(lt2) + cos(lt1)*cos(lt2)*cos(lg1-lg2))
print(round(d, 2))

