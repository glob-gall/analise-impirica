e = input("em qual escala se encontra: C ou F: ")
t = float(input("Qual o valor da temperatura?: "))

if(e == "F"):
	c = (5/9)*(t-32)
	print(round(c, 2))
else:
	f = 1.8*t+32
	print(round(f, 2))