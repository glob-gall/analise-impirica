"""
Ordem Crescente
"""
a = int(input("Digite um primeiro numero: "))
b = int(input("Digite um segundo numero: "))
c = int(input("Digite um terceiro numero: "))
me = min(a, b, c)
ma = max(a, b, c)
mi = a + b + c - me - ma
print(me)
print(mi)
print(ma)
