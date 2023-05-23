import unittest
import sys
import io
from math import pi


def verificar_string(string1, valores_entrada):
    # Abre o arquivo 'codigo.py' e lê o seu conteúdo
    with open('3451_2445_2927.py', 'r') as file:
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

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    return string1 == valor_impresso1


class TestStringVerification(unittest.TestCase):
    def test_verificar_string_1(self):
        valores_entrada = ["F", "100.0"]
        self.assertTrue(verificar_string("37.78", valores_entrada))

    def test_verificar_string_2(self):
        valores_entrada = ["C", "320.0"]
        self.assertTrue(verificar_string("608.0", valores_entrada))

    def test_verificar_string_3(self):
        valores_entrada = ["F", "30.0"]
        self.assertTrue(verificar_string("-1.11", valores_entrada))


if __name__ == '__main__':
    unittest.main()
