a = float(input())
lim = 10000

if (a <= lim):
	total = a * 5
	print(round(total,2))
	
else:
	total = lim * 5 + 4 * (a - lim)
	print(round(total,2))