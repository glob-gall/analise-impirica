n = int(input())
h=0
for i in range(1,n + 1):
	s = (-1) ** (i - 1)
	h = s * (1 / i) + h
print("H =",round(h,6))