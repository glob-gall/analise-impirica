# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*

a = float(input("Digite o valor do comprimento do lado a do triangulo;"))
b = float(input("Digite o valor do comprimento do lado b do triangulo;"))
c = float(input("Digite o valor do comprimento do lado c do triangulo;"))

s = (a+b+c) / 2
area = sqrt(s*(s-a)*(s-b)*(s-c))

print(round(area,5))
