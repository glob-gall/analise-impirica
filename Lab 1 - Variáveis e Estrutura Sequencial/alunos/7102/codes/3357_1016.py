from math import *

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

S = (a + b + c) / 2
A = sqrt( S * (S - a) * (S - b) * (S - c))
print(round(A, 5))
