escala = input("Digite a escala da temperatura (C para Celsius, F para Fahrenheit): ")
temperatura = float(input("Digite o valor da temperatura: "))

if escala.upper() == "C":
    temperatura_convertida = (temperatura * 9/5) + 32
elif escala.upper() == "F":
    temperatura_convertida = (temperatura - 32) * 5/9
else:
    print("Escala inválida.")

temperatura_convertida = round(temperatura_convertida, 2)
print("Temperatura convertida:", temperatura_convertida)
