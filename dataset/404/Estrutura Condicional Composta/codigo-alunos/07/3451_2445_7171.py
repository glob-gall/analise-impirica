#conversão

escala= input(" Digite a escala da temperatura (C/F):").lower()
temp= float(input( " Digite o valor da temperatura:"))

if (escala == "c"):
	f= (9*temp)/5 + 32
	print(round(f, 2))
	
else:
	c= (5/9)* (temp - 32)
	print(round(c, 2))