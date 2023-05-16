# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input("digite um numero: "))
y = int(input("digite um numero: "))
z = int(input("digite um numero: "))

maximo = max(x,y,z)
minimo = min(x,y,z)
meio = (x+y+z) - maximo - minimo

print(minimo)
print(meio)
print(maximo)