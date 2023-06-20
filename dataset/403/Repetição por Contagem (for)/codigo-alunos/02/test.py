import unittest
import sys
import io
from math import pi


def verificar_string(string1, valores_entrada,arquivo):
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

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    return string1 == valor_impresso1


class TestStringVerification(unittest.TestCase):
    file = 'codigo.py'
    def test_verificar_string_1(self):
        valores_entrada = [["10","10","9"], ["44","45","46"], "60"]
        self.assertTrue(verificar_string(["2", "0", "1"], valores_entrada,self.file))

    def test_verificar_string_2(self):
        valores_entrada = [["9.36","5.04","1.95","2.16","2.49","9.42","5.36","1.92","4.59","1.99"], ["24","33","21","59","32","7","81","54","69","79"], "100"]
        self.assertTrue(verificar_string(["1", "1", "8"], valores_entrada,self.file))

    def test_verificar_string_3(self):
        valores_entrada = [["0.44","3.62","1.85","6.84","6.73","8.67","1.44","7.46","4.15","5.46"], ["72","58","52","30","63","39","67","4","65","60"], "75"]
        self.assertTrue(verificar_string(["2", "4", "4"], valores_entrada,self.file))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestStringVerification.file = sys.argv.pop()
    unittest.main()
