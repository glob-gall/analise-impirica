t= input("temperatura: ")
vt= float(input("Digite o valor: "))

if(t=="F"):
	C=(5/9)*(vt-32)
	print(round(C,2))
else:
	F=(9/5)*vt+32
	print(round(F,2))
