import unittest
import observer

class TesteStrategy(unittest.TestCase):

    def setUp(self):
        self.dados = [6, 9, 3, 8, 2]

    def test_InstanciaObserver(self):
        ob = observer.Observer()
        erro = 'objeto nao e instancia da classe'
        self.assertIsInstance(ob, observer.Observer, erro)

    def test_ContadorDePalavras(self):
        resultado = observer.contador_de_palavras('este teste possui seis palavras')
        self.assertEqual(resultado, 6)

    def test_Contador_De_Palavras_Pares(self):
        resultado2 = observer.contador_de_palavras_pares('este teste possui seis palavras')
        self.assertEqual(resultado2, 3)

    def test_Contador_De_Palavras_Maiusculas(self):
        resultado2 = observer.contador_palavras_maisculo('este Teste possui Seis Palavras')
        self.assertEqual(resultado2, 3)


if __name__ == '__main__':
    unittest.main()
