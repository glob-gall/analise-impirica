from math import*
a= float(input())
b=float(input())
gama=radians(float(input()))

c=sqrt((a**2)+(b**2)-2*a*b*cos(gama))

print(round(c, 2))