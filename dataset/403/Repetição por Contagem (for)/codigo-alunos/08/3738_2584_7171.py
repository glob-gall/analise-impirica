#alteração de sinal

n=int(input("Digite o numero:"))

H=0
j=1
sinal= +1
for i in range(n):
	H= H+ sinal*1/j
	sinal= -sinal
	j= j+1
print("H =",round(H,6))