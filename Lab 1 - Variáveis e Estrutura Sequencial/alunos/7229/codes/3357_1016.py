from math import *

var1=float(input())
var2=float(input())
var3=float(input())

var4=(var1+var2+var3)/2
var5=sqrt(var4*(var4-var1)*(var4-var2)*(var4-var3))

print(round(var5,5))