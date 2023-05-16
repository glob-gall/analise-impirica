# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input())
b = int(input())
c = int(input())

A = min(a, b, c)
C = max(a, b, c)
B = a + b + c - A - C

print(A)
print(B)
print(C)
