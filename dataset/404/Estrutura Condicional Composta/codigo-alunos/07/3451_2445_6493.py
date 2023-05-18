tipo=input("insira qual a escala: ")
tipo = tipo.upper()
temperatura=float(input("Insira a temperatura em celsius: "))
valor=0
if tipo=="F":
	valor=5/9*(temperatura-32)
elif tipo=="C":
	valor=1.8*temperatura+32
print(round(valor,2))