A = float(input("area: "))
if (A <= 10000):
	C = 6
	F = 100
	v = A * C + F 
elif( A > 10000 and A <=20000):
	C = 5.5
	F = 150
	v = A * C + F 
elif(A> 20000 and A <=30000):
	C = 5
	F = 200
	v = A * C + F
elif(A>30000):
	C = 4.5
	F = 250
	v = A*C+F
print(round(v,2))