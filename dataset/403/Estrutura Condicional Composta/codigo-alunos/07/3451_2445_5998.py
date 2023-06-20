escala = input("Digite a escala de medicao de temperatura: ").upper()
valor = float(input("Digite o valor da temperatura: "))

if escala == "C":
	x = ((9*valor)/5)+32
	
elif escala == "F":
	x = 5/9*(valor - 32)
	
print(round(x,2))