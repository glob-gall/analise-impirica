v1 = int(input("Qual a quantidade de votos do candidato mais votado? "))
v2 = int(input("Digite a quantidade de votos do candidato em segundo lugar: "))
mv = int(input("Qual o numero de votos do candidato com menos votos? "))
tv = v2+mv

if(abs(v1)<=tv):
	print("SIM")
else:
	print("NAO")