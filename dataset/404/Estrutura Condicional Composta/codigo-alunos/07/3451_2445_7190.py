from math import*

e = input("escala: ").upper()
v = float(input("temperatura: "))


c = 5*(v-32)/9
f = v*9/5+32



if(e == "F"):
	print(round(c,2))

if(e == "C"):
	print(round(f,2))



