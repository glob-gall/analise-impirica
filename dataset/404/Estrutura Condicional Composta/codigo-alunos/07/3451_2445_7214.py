escala = input("Qual a escala da temperatura? ").upper()
temperatura = float(input("Digite o valor da temperatura: "))

if(escala== "F"):
	codigo = 5/9 * (temperatura-32)
else:
	codigo = 9/5 * temperatura + 32 
	
print(round(codigo,2))
	