mav = int(input("Candidato mais votado: "))
sl = int(input("Segundo lugar: "))
mev = int(input("Menos votado: "))
s = mav + sl + mev
if mav > (s/2):
	print("NAO")
else:
	print("SIM")