# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import*
# Leitura de entradas
ladoa = float(input("Digite os tres comprimentos dos lados:"))
ladob = float(input())
ladoc = float(input())

s = (ladoa + ladob + ladoc) / 2
area = sqrt(s*(s-ladoa)*(s-ladob)*(s-ladoc))

#Impressao de saidas
print(round(area, 5))

