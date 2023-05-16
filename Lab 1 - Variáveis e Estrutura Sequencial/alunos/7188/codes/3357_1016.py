from math import*

var= float(input("comprimento1"))
var2=float(input("comprimento2"))
var3=float(input("comprimento3"))

S= (var+var2+var3)/2
A= (sqrt(S*(S-var)*(S-var2)*(S-var3)))

print(round(A,5))