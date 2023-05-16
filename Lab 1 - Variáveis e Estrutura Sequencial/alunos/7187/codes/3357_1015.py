# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("insira um numero "))
b = int(input("insira um numero "))
c = int(input("insira um numero "))
menor = min(a,b,c)
maior = max(a,b,c)
soma = a + b + c
intermediario = soma - menor - maior
print (menor)
print (intermediario)
print (maior)