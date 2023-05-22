import unittest
import sys
import io
import os

def verificar_string(string1, string2, valores_entrada,arquivo):
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

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    return string1 == saida1 and string2 == saida2

def openAllFiles():
    files = os.listdir('./')
    files.remove('test.py')
    return files



class TestStringVerification(unittest.TestCase):
    files = openAllFiles()
    
    def test_all_files(self):
        def test_verificar_string_1(self,arquivo):
            valores_entrada = ["2.0"]
            self.assertTrue(verificar_string("12.566", "33.51", valores_entrada,arquivo))

        def test_verificar_string_2(self,arquivo):
            valores_entrada = ["0.1"]
            self.assertTrue(verificar_string("0.031", "0.004", valores_entrada,arquivo))

        def test_verificar_string_3(self,arquivo):
            valores_entrada = ["11.0"]
            self.assertTrue(verificar_string("380.133", "5575.28", valores_entrada,arquivo))
        
        for f in self.files:
            # print(f)
            test_verificar_string_1(self,f)
            test_verificar_string_2(self,f)
            test_verificar_string_3(self,f)



if __name__ == '__main__':
    unittest.main()
