x = input("escala: ").upper()
y = float(input("temperatura: "))
if(x=="F"):
	C=(5/9)*(y-32)
	print(round(C,2))
else:
	F=(9/5)*y+32
	print(round(F,2))
	
