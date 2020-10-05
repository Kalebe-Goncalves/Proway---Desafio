import unittest
import main
import bd

"""
Código responsável pelos teste unitários do código
"""


class Verificar_atualizar_min(unittest.TestCase):
    """
    Classe que contém os métodos testes no padrão arrange, act e assert
    """

    def test_retorna_lista_min_tamanho1(self):
        """
        Teste que verifica se o recorde minimo foi quebrado funciona corretamente
        """
        # arrange
        placar = 12
        min_temp = 0
        q_recor_min = 0

        # act
        teste = len(main.atualizar_min(placar, min_temp, q_recor_min))

        # assert
        self.assertEqual(1, teste)

    def test_retorna_lista_min_tamanho2(self):
        """
        Teste que verifica se o recorde minimo foi quebrado funciona corretamente
        """
        placar = 10
        min_temp = 12
        q_recor_min = 0

        teste = len(main.atualizar_min(placar, min_temp, q_recor_min))

        self.assertEqual(2, teste)

    def test_retorna_lista_max_tamanho1(self):
        """
        Teste que verifica se o recorde maximo foi quebrado funciona corretamente
        """
        placar = 12
        max_temp = 0
        q_recor_max = 0

        teste = len(main.atualizar_max(placar, max_temp, q_recor_max))

        self.assertEqual(1, teste)

    def test_retorna_lista_max_tamanho2(self):
        """
        Teste que verifica se o recorde maximo foi quebrado funciona corretamente
        """
        placar = 24
        max_temp = 12
        q_recor_max = 0

        teste = len(main.atualizar_max(placar, max_temp, q_recor_max))

        self.assertEqual(2, teste)

    def test_gravar_dados_bd(self):
        """
        Teste que verifica se a gravação do banco de dados acontece corretamente
        """
        jogo = 1
        placar = 12
        minimo = 0
        maximo = 0
        rec_min = 0
        rec_max = 0

        teste = main.gravar_dados_bd(
            jogo, placar, minimo, maximo, rec_min, rec_max)

        self.assertTrue(teste)

    def test_retornar_valores_bd(self):
        """
        Teste que verifica o retorno da função está correto
        """
        bd_teste = type(bd.Partida.select())

        teste = type(main.retornar_valores_bd())

        self.assertEqual(bd_teste, teste)

    def test_inserir_dados(self):
        """
        Teste que verifica se a inserção de dados localmente (sem ser no banco de dados) acontece corretamente
        """
        jogo = 2
        placar = 24
        min_temp = 12
        max_temp = 12
        q_recor_min = 0
        q_recor_max = 1

        teste = main.inserir_dados(
            placar, jogo, min_temp, max_temp, q_recor_min, q_recor_max)

        self.assertTrue(teste)

    def teste_gerar_planilha(self):
        """
        Teste que verifica a criação/atualização da planilha
        """

        teste = main.exportar_planilha_excel()

        self.assertTrue(teste)
