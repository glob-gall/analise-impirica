from math import*

a = float(input("L1: "))
b = float(input("L2: "))
c = float(input("L3: "))

s = (a+b+c)/2

A = sqrt(s*(s-a)*(s-b)*(s-c))

print(round(A,5))