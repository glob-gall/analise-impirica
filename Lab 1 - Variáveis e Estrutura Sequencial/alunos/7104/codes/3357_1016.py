from math import*
a=float(input())
b=float(input())
c=float(input())

s=(a+b+c)/2
a=sqrt(s*(s-a)*(s-b)*(s-c))

print(round(a, 5))
