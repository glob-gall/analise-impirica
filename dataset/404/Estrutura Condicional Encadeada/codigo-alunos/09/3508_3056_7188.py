vs= float(input())
if vs>0:
	if vs>0 and vs<=10000:
		ct= 6
		ft= 100
	elif vs>10000 and vs<=20000:
		ct= 5.5
		ft= 150
	elif vs>20000 and vs<=30000:
		ct= 5.5
		ft= 200
	else:
		ct=4.5
		ft=250
	va= (vs)* (ct) + (ft)
	print(round(va,2))