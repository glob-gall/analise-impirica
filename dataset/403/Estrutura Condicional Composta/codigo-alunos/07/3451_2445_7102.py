nome = input()
t = float(input())

if (nome.upper() == "F"):
	a = 5 / 9 * (t - 32)
	print(round(a,2))
	
else:
	a = (9 / 5 * t) + 32
	print(round(a,2))
	