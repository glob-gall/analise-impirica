import math

lado_a = float(input("Digite o comprimento do lado a: "))
lado_b = float(input("Digite o comprimento do lado b: "))
lado_c = float(input("Digite o comprimento do lado c: "))

semiperimetro = (lado_a + lado_b + lado_c) / 2
area = math.sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c))

area_arredondada = round(area, 5)

print(area_arredondada)
