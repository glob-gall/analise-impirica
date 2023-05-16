num1 = int(input("digite um numero inteiro: "))
num2 = int(input("digite outro numero inteiro: "))
num3 = int(input("digite mais um numero inteiro: "))

var1 = min(num1, num2, num3)
var3 = max(num1, num2, num3)
var2 = (num1 + num2 + num3) - var1 - var3


print(var1)
print(var2)
print(var3)