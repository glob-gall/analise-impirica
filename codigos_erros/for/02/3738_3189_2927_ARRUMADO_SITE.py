import numpy as np

medias = np.array(eval(input()))
presenca = np.array(eval(input()))
carga_horaria = int(input())

aprovados = 0
reprovados_nota = 0
reprovados_freq = 0

for i in range(len(medias)):
    if medias[i] >= 5.0 and presenca[i] >= 0.75 * carga_horaria:
        aprovados += 1
    elif medias[i] < 5.0:
        reprovados_nota += 1
    else:
        reprovados_freq += 1

resultado = np.array([aprovados, reprovados_nota, reprovados_freq])
print(resultado)
