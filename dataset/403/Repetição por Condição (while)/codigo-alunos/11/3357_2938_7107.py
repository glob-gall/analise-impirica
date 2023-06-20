from math import *

d1 = float(input())
d2 = float(input())
a = radians(float(input()))

l3 = sqrt((d1 ** 2 + d2 **2) - (2*d1*d2) * cos(a))

print(round(l3, 2))