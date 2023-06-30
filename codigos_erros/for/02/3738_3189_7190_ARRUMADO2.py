import numpy as np

medias_finais = np.array(eval(input("Digite as médias finais dos alunos: ")))
frequencias = np.array(eval(input("Digite as frequências dos alunos: ")))
carga_horaria = int(input("Digite a carga horária da disciplina: "))

num_alunos_aprovados = 0
num_alunos_reprovados_nota = 0
num_alunos_reprovados_frequencia = 0

for i in range(len(medias_finais)):
    if medias_finais[i] >= 5.0 and frequencias[i] >= (0.75 * carga_horaria):
        num_alunos_aprovados += 1
    elif medias_finais[i] < 5.0:
        num_alunos_reprovados_nota += 1
    else:
        num_alunos_reprovados_frequencia += 1

resultado = np.array([num_alunos_aprovados, num_alunos_reprovados_nota, num_alunos_reprovados_frequencia])

print("Resultado:")
print(resultado)
