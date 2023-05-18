mais = int(input("candidato mais votado:  "))
seg =  int(input("candidato em segundo lugar:  "))
menos = int(input("candidato menos votado:  "))

if mais>(seg+menos):
	print("NAO")
	
else:
	print("SIM")