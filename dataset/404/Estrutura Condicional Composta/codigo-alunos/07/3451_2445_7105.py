escala = input()
escala = escala.upper()
temperatura = float(input())


if(escala == "C"):
	fahre = (9*temperatura/5) + 32
	print(round(fahre, 2))
else:
	c = (5/9)*(temperatura-32)
	print(round(c,2))
	