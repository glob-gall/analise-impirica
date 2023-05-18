a = float(input("area:"))

c =a*6+100
v =a*5.5+150
b =a*5+200
n =a*4.5+250


if(0<=a<=10000):
	print(round(c,2))
if(10000<a<=20000):
	print(round(v,2))
if(20000<a<=30000):
	print(round(b,2))
if(30000<a):
	print(round(n,2))