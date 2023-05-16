# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

m = int(input("N1: "))
n = int(input("N2: "))
o = int(input("N3: "))

a = min(m,n,o)
b = max(m,n,o)
c = (m + n + o) - (a + b)

print(a)
print(c)
print(b)