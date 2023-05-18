vot1 = int(input("Mais votado: "))
vot2 = int(input("Segundo lugar: "))
vot3 = int(input("Menos votado: "))
medvot1 = vot1/3
med2 = vot2/3
med3 = vot3/3
if 		medvot1>med2 + med3:
			print("NAO")

else:
			print("SIM")
			