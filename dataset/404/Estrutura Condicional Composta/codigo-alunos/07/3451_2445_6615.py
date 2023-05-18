esc = input("digite a escala termometrica: ").upper()
var = float(input("digite o valor da temperatura: "))
CL = 5/9*(var - 32)
FH = (9*var)/5 + 32

if (esc == "F"):
	print(round(CL,2))
else:
	print(round(FH,2))