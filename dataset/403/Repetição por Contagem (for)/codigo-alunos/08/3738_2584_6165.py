n = int(input())
soma = 0
sinal = +1

for i in range(1, n + 1):
	soma = soma + sinal/i
	sinal = -sinal
print("H =", round(soma,6))