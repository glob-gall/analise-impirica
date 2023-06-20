n=input("ingrediente:").upper()
q=int(input("quantidade:"))
if(n=="ARROZ"and q>0 and q<50):
	x=500
	print(x*q)
elif(n=="CENOURA"and q>0 and q<50):
	x=100
	print(x*q)
elif(n=="KAMPYO"and q>0 and q<50):
	x=20
	print(x*q)
elif(n=="NORI"and q>0 and q<50):
	x=50
	print(x*q)
elif(n=="OMELETE"and q>0 and q<50):
	x=200
	print(x*q)
elif(n=="PEPINO"and q>0 and q<50):
	x=150
	print(x*q)
elif(n=="SALMAO"and q>0 and q<50):
	x=300
	print(x*q)
elif(n=="SHITAKE" and q>0 and q<50):
	x=150
	print(x*q)
else:
	print("Entrada invalida")
	