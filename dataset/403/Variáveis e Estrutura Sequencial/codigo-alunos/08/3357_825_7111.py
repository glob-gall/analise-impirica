# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import*

# Leitura de entrada
r = float(input("Digite o valor do raio:"))
area = pi * r ** 2
volume = 4 / 3 * pi * r ** 3 

# Impressao de saidas
print (round(area, 3))
print (round(volume, 3))