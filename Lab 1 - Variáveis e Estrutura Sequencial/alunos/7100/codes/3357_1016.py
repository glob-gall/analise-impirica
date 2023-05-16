a = float(input("Digite um comprimento: "))
b = float(input("Digite outro comprimento: "))
c = float(input("Digite mais um comprimento: "))

from math import *

s = (a + b + c) / 2
A = sqrt(s * (s - a) * (s - b) * (s-c))

print(round(A,5))