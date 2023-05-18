hec=float(input("Insira a area a ser trabalhada: "))
if hec<=10000:
	valor=hec*5
else:
	hec-=10000
	valor=50000+hec*4
print(round(valor,2))