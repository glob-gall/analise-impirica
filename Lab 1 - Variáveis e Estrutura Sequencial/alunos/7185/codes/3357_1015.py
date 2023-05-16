# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

x = int(input("Digite um numero inteiro: "))
y = int(input("Digite um numero inteiro: "))
z = int(input("Digite um numero inteiro: "))
intermed = ((x + y + z)- min(x,y,z)) - max(x,y,z)
print (min(x,y,z))
print (intermed)
print (max(x,y,z))