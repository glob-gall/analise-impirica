# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a=float(input("area a"))
b=float(input("area b"))
c=float(input("area c"))
s=(a+b+c)/2
x=(s*(s-a)*(s-b)*(s-c))**0.5
print(round(x,5))
