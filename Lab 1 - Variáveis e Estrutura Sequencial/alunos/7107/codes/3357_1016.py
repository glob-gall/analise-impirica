from math import *

l1 = float(input())
l2 = float(input())
l3 = float(input())

s = (l1 + l2 + l3) / 2

cA = s*(s - l1)*(s - l2)*(s - l3)

A = sqrt(cA)

print(round(A, 5))