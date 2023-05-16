nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media_ponderada = (nota1*1 + nota2*2 + nota3*3 + nota4*4) / (1+2+3+4)
media_arredondada = round(media_ponderada, 2)

print(media_arredondada)
