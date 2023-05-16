# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("entra valo a: "))
b = int(input("entra valo b: "))
c = int(input("entra valo c: "))
maior = max(a,b,c)
menor = min(a,b,c)
meio = a+b+c-menor-maior
print(menor)
print(meio)
print(maior)