t =input("Digite escala da temperatura: ").upper()
v = float(input("Digite o valor da temperatura: "))
F = (1.8 * v) + 32
C = (v-32)/1.8
if t == "C":
	print(round(F,2))
else:

	print(round(C,2))