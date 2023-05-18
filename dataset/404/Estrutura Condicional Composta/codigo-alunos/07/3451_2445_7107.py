op = input().upper()
vt = float(input())

if(op == 'C'):
	F = (vt * (9/5) + 32)
	print(round(F, 2))
	
else:
	C = (5/9)*(vt - 32)
	print(round(C, 2))