a = float(input("digite o valor de um lado: "))
b = float(input("digite o valor de outro lado: "))
c = float(input("digite o valor de mais um lado: "))

from math import * 

s = (a+b+c)/2

A = sqrt(s*(s - a)*(s - b)*(s - c))

print(round(A, 5))