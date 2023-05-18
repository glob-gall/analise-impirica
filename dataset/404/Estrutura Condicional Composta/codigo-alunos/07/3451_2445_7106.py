rep = input("Qual representacao deseja: ").lower()
temp = float(input("Escreva a temperatura para conversao:  "))
c = 5/9*(temp - 32)
f = temp*(9/5)+32
if rep == "c":
	print(round(f, 2))
else:
	print(round(c, 2))
	
