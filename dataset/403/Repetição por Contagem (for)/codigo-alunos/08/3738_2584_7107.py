n = int(input())
h = 0
c = 0

for i in range(n):
	c = c + 1

	h = (1 * ((-1) ** i ) / c) + h
	
	
print("H =", round(h, 6))