mais= int(input('candidato mais votado: '))
seg= int(input('segundo lugar: '))
menos= int(input('candidato menos votado: '))

if mais>seg+menos:
	print('NAO')
else:
	print('SIM')