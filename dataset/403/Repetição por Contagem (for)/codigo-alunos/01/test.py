import unittest
import sys
import io
from math import pi


def verificar_string(string1, string2, string3, valores_entrada,arquivo):
    # Abre o arquivo 'codigo.py' e lê o seu conteúdo
    with open(arquivo, 'r') as file:
        codigo = file.read()

    # Redireciona a saída padrão para um objeto io.StringIO
    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    # Cria um iterador para fornecer os valores de entrada sequencialmente
    input_mock = iter(valores_entrada)

    # Função de input mockada para retornar os valores do iterador
    def input_mock_function(*args):
        return next(input_mock)

    try:
        # Executa o código lido do arquivo com o input mockado
        exec(codigo, {'input': input_mock_function})
        valor_impresso1 = sys.stdout.getvalue().strip()
        partes = valor_impresso1.split('\n')
        saida1 = partes[0]
        saida2 = partes[1]
        saida3 = partes[2]

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    if(saida3 == "zero"):
        return string1 == saida1 and string2 == saida2
    else:
        return string1 == saida1 and string2 == saida2 and string3 == saida3


class TestStringVerification(unittest.TestCase):
    file = 'codigo.py'
    def test_verificar_string_1(self):
        valores_entrada = ["60.0","73.9","22.9","72.1","72.0","100.6"]
        self.assertTrue(verificar_string("1", "3", "2", valores_entrada,self.file))

    def test_verificar_string_2(self):
        valores_entrada = ["11.6","60.6","16.6","11.35"]
        self.assertTrue(verificar_string("2", "1", "zero", valores_entrada,self.file))

    def test_verificar_string_3(self):
        valores_entrada = ["72.9","29.1","7.29","90.7","66.6"]
        self.assertTrue(verificar_string("3", "1", "zero", valores_entrada,self.file))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestStringVerification.file = sys.argv.pop()
    unittest.main()
