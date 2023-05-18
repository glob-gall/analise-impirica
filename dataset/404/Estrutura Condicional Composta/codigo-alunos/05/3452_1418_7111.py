mv= int (input("maiores votos?"))
sl= int (input("segundo mais votado?"))
mev= int (input("menores votos:"))

x = mv + sl + mev
y = x / 2

if(mv<=y):
	print("SIM")
if(mv>y):
	print("NAO")
