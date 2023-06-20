e = input("qual a escala").upper()
t = float(input("qual a temperatura"))

if(e =="F"):
	C = (5/9)*(t-32)
	print(round(C,2))
else:
	F = (9/5)*t+32
	print(round(F,2))
	