t = input("escala temp: ")
Vt = float(input("valor da temp: "))

if (t == "F"):
	
	C = 5/9*(Vt -32)
if (t == "C"):
	
	C = Vt * 1.8 + 32
	
print(round(C,2))