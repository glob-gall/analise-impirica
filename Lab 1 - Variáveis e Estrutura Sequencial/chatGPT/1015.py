num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

menor = min(num1, num2, num3)
maior = max(num1, num2, num3)
intermediario = num1 + num2 + num3 - menor - maior

print(menor)
print(intermediario)
print(maior)
