import ast
import csv
import glob
from radon.raw import analyze as raw_analyze
from radon.complexity import cc_visit

# Função para contar as variáveis em um nó da árvore sintática
def contar_variaveis(node):
    if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load):  # Verifica se é uma atribuição de variável
        return 1
    else:
        return sum(contar_variaveis(child) for child in ast.iter_child_nodes(node))

# Obtém todos os arquivos .py no diretório atual
file_list = glob.glob('*.py')

# Exclui os arquivos com nomes específicos da lista
excluded_files = ['test.py', 'calcular_complexidade.py', 'test_all.py']
file_list = [filename for filename in file_list if filename not in excluded_files]

# Abre o arquivo CSV para escrita
with open('metrics.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Escreve o cabeçalho do arquivo CSV
    writer.writerow(['Arquivo', 'LOC', 'LLOC', 'SLOC', 'Linhas de Comentário', 'Linhas em Branco', 'Complexidade Ciclomática', 'Número de Variáveis'])

    for filename in file_list:
        try:
            with open(filename, 'r') as file:
                source_code = file.read()

            # Cálculo das métricas brutas
            raw_metrics = raw_analyze(source_code)
            loc = raw_metrics.loc
            lloc = raw_metrics.lloc
            sloc = raw_metrics.sloc
            comment_lines = raw_metrics.comments
            blank_lines = raw_metrics.blank

            # Contagem das variáveis
            parsed_code = ast.parse(source_code)
            num_variaveis = contar_variaveis(parsed_code)
            
            # Cálculo da complexidade ciclomática
            # Corrige a indentação do código
            source_code = source_code.expandtabs()

            # Adiciona um nível de indentação
            source_code = '\n'.join(f'    {line}' for line in source_code.splitlines())
            code_wrapper = f"def calculate_complexity():\n{source_code}"
            results = cc_visit(code_wrapper, no_assert=True)
            total_complexity = sum(result.complexity for result in results)


            # Escreve os dados no arquivo CSV
            writer.writerow([filename, loc, lloc, sloc, comment_lines, blank_lines, total_complexity, num_variaveis])

        except Exception as e:
            print(f"Erro ao processar o arquivo {filename}: {str(e)}")
            writer.writerow([filename, 0, 0, 0, 0, 0, 0, 0])

print("Dados exportados para metrics.csv")

