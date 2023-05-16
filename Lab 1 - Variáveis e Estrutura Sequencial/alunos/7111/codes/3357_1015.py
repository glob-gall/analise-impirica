# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# Leitura de entradas
prim = int(input("digite tres numeros:"))
segun = int(input())
terc = int(input())
conj= (prim, segun, terc)
menor = int (min(conj))
maior = int (max(conj))
intermed = int( (prim + segun + terc - menor - maior) )

# Impressao de saidas
print (menor)
print (intermed)
print (maior)