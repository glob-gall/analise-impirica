a=float(input())

if(a<=10000):
	print(round(a*5,2))

else:
	v=10000*5+((a-10000)*4)
	print(round(v,2))