c1 = int(input("mais votado: "))
c2 = int(input("segundo lugar: "))
c3 = int(input("menos votado: "))

x = (c1+c2+c3)/2

if(c1>x):
	print("nao".upper())
else:
	print("sim".upper())

