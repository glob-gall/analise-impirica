# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("Digite um numero para a:"))
b = float(input("Digite um numero para b:"))
c = float(input("Digite um numero para c:"))
semi = (a + b + c) / 2
area = (semi*(semi-a)*(semi-b)*(semi-c))**0.5
print(round(area, 5))