esc = input("Digite aqui: ")
vtemp = float(input("Digite o valor da temperatura: "))
print("")
if (esc.upper() == "F"):
	conv = (vtemp - 32) * (5/9)
	print (round(conv, 2))
if (esc.upper() == "C"):
	conv = (vtemp * 1.8) + 32
	print (round(conv, 2))