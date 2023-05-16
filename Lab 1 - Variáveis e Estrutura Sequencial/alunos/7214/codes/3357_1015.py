# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = int(input("Qual o valor de a?"))
b = int(input("Qual o valor de b?"))
c = int(input("Qual o valor de c?"))

menor = min(a,b,c)
maior = max(a,b,c)
intermediario = a+b+c-menor-maior

print(menor)
print(intermediario)
print(maior)