
from math import *

a = float(input("insira um numero "))
b = float(input("insira um numero "))
c = float(input("insira um numero "))

s = (a + b + c) / 2
a = sqrt(s * (s - a) * (s - b) * (s - c))

print(round(a, 5))

