a = input("Qual e a escala: ").upper()
t = float(input("Valor da temperatura: "))
if (a == "F"):
	c = 5/9 * (t - 32)
	print(round(c,2))
else:
	f = (9/5) * t + 32
	print(round(f,2))