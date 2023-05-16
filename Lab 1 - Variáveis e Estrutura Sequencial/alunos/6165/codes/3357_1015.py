# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
na = int(input("qual o valor de na? "))
nb = int(input("qual o valor de nb? "))
nc = int(input("qual o valor de nc? "))

n1 = min(na, nb, nc)
n2 = max(na, nb, nc)
vm = na+nb+nc-n1-n2

print(n1)
print(vm)
print(n2)