from math import*

a= radians(float(input("latitude t1")))
b= radians(float(input("latitude g1")))
c= radians(float(input("latitude t2")))
d= radians(float(input("latitude g2")))

R= 6371.01
D= R*acos(sin(a)*sin(c)+cos(a)*cos(c)*cos(b-d))

print(round(D,2))