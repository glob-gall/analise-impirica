from math import*
a=float(input("escreva p1"))
b=float(input("escreva p2"))
c=float(input("escreva p3"))
s=(a+b+c)/2
a=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(a,5))
