# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = int(input("numero1: "))
b = int(input("numero2: "))
c = int(input("numero3: "))

Min= min(a,b,c)
Max= max(a,b,c)
Med= (a+b+c)- Min - Max

print(Min)
print(Med)
print(Max)

