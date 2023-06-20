a= float(input("area em hectares"))
if a<= 10000:
	print(a*5)
else:
	print(10000*5 + (a-10000)*4)