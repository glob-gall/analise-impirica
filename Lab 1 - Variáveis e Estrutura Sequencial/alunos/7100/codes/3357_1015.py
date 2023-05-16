a = int(input("Digite um valor inteiro: "))
b = int(input("Digite outro valor inteiro: "))
c = int(input("Digite mais um valor inteiro: "))

A = min(a, b, c)
C = max(a, b, c)
B = (a + b + c) - A - C
print(A)
print(B)
print(C)