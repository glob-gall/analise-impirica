a = float(input("digite a area: "))

if a <= 10000:
	v = a*5
	
else:
	ex = a-10000
	v = (5*10000) + (4*ex)
	
print(round(v,2))