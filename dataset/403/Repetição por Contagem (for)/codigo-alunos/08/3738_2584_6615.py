N = int(input("numero: "))
l = 1
H = 0
sinal = +1
for i in range(N):
	H = H + sinal *1/l 
	sinal = -sinal
	l = l+1
print("H =", round(H,6))