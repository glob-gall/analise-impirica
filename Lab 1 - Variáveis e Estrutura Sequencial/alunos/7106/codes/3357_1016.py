from math import *
a = float(input("Escreva o primeiro numero: "))
b = float(input("Escreva o segundo numero: "))
c = float(input("Escreva o terceiro numero: "))
semi = (a+b+c)/2
area = sqrt(semi*(semi-a)*(semi-b)*(semi-c))
print(round(area, 5))