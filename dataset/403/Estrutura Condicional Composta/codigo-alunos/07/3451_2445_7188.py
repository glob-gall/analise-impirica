tp= input("temperatura").upper()
vt= float(input("valor da temperatura"))
if(tp== "C"):
	g= (1.8* vt) + 32
	print(round(g,2))
else:
	c= (5/9* (vt - 32))
	print(round(c,2))
	