# Teste seu codigo aos poucos.
dig = int(input("primeiro: "))
dog = int(input("segundo: "))
dug = int(input("terceiro: "))
maior = max(dig , dog ,dug)
menor  = min(dig , dog , dug)
med = dig + dog + dug - menor - maior

# Nao teste tudo no final, pois fica mais dificil de identificar erros.
print(menor , med , maior)
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
