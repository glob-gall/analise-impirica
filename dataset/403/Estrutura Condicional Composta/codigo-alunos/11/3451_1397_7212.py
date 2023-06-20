area= float(input())

if(area<=10000):
	print(round(area*5,2))
else:
	v=10000*5+((area-10000)*4)
	print(round(v,2))
	