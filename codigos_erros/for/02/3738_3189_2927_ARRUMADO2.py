import numpy as np

notas = np.array(eval(input()))
freq = np.array(eval(input()))
carga = int(input())

vcont = np.zeros(3, dtype=int)

for i in range(len(notas)):
    if freq[i] < 0.75 * carga:
        vcont[2] += 1  # Aluno reprovado por frequência
    elif notas[i] >= 5.0:
        vcont[0] += 1  # Aluno aprovado
    else:
        vcont[1] += 1  # Aluno reprovado por nota

print(vcont)
