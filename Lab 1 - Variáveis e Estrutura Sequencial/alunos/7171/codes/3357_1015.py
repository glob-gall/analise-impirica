# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

ent1= int(input("Digite 3 numeros:"))
ent2= int(input())
ent3= int (input())
numeros= (ent1, ent2, ent3)
menor= min (numeros)
maior= max (numeros)
mid= ((ent1 + ent2 + ent3)- menor - maior)

print(menor)
print( mid)
print(maior)