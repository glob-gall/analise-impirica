hec=float(input("Insira a area a ser trabalhada: "))
if hec<=1000:
	comi=hec*0.05
else:
	hec-=1000
	comi=50+hec*0.1
print(round(comi,2))