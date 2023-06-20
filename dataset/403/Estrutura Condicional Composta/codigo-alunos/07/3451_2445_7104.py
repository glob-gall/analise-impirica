escala = input()
temperatura = float(input())

if(escala == "C"):
	c = 9/5*temperatura + 32
	print(round(c,2))
else:
	c = 5/9*(temperatura - 32)
	print(round(c,2))