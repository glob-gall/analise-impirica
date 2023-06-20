from math import*
a=float(input("a:"))
b=float(input("b:"))
y=float(input("y:"))
c=((a**2)+(b**2)-2*a*b*cos(radians(y)))**0.5
print(round(c,2))