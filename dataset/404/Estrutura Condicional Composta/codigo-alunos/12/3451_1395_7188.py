vv= float(input("valor de vendas"))
if vv <= 1000:
	print(round(vv*0.05,2))
else:
	print(round(1000*0.05+ (vv-1000)*0.10,2))
	