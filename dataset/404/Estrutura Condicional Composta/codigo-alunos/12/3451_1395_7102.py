a = float(input())
lim = 1000

if (a <= lim):
	total = a * 0.05
	print(round(total,2))
	
else:
	total = lim * 0.05 + 0.1 * (a - lim)
	print(round(total,2))