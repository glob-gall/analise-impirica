import unittest
import sys
import io


def verificar_string(string,arquivo):
    # Abre o arquivo 'codigo.py' e lê o seu conteúdo
    with open(arquivo, 'r') as file:
        codigo = file.read()

    # Redireciona a saída padrão para um objeto io.StringIO
    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    try:
        # Executa o código lido do arquivo
        exec(codigo)

        # Obtém o valor impresso durante a execução
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
    file = 'codigo.py'
    def test_verificar_string(self):
        self.assertTrue(verificar_string("45.0",self.file))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestStringVerification.file = sys.argv.pop()
    unittest.main()

