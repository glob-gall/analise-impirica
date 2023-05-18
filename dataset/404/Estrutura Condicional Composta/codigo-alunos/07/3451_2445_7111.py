E = input("Qual a escala?")
T = float (input("Qual a temperatura?"))
C= (5/9) * (T - 32)
F = T * (9/5) + 32
if (E == "F"):
	print(round(C,2))
else:
	print (round(F,2))