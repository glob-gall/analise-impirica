vv = float (input("Qual o valor vendido?"))
vf1= (vv * 0.05)
e = vv - 1000
vf2 = (0.05 * 1000) + (e * 0.10)
if (vv <= 1000):
	print (round(vf1, 2 ))
else:
	print (round(vf2,2))