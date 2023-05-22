import unittest
import sys
import io


def verificar_string(string, valores_entrada):
    # Abre o arquivo 'codigo.py' e lê o seu conteúdo
    with open('codigo.py', 'r') as file:
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

        valor_impresso = sys.stdout.getvalue().strip()

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se o valor impresso é igual à string fornecida
    return string == valor_impresso


class TestStringVerification(unittest.TestCase):
    def test_verificar_string_1(self):
        valores_entrada = ["Python"]
        self.assertTrue(verificar_string("Python", valores_entrada))

    def test_verificar_string_2(self):
        valores_entrada = ["Donald"]
        self.assertTrue(verificar_string("Donald", valores_entrada))

    def test_verificar_string_3(self):
        valores_entrada = ["Gandalf"]
        self.assertTrue(verificar_string("Gandalf", valores_entrada))


if __name__ == '__main__':
    unittest.main()
