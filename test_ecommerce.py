import unittest
from ecommerce import calcular_desconto 

class TestQualidade(unittest.TestCase):

    def test_regra_100_reais(self):
        # TESTE VERDE: 100 reais deve resultar em 90
        self.assertEqual(calcular_desconto(100), 90.0)

    def test_cupom_especial(self):
        # TESTE VERDE: Cupom QUERO20 em compra de 50 deve resultar em 40
        self.assertEqual(calcular_desconto(50, "QUERO20"), 40.0)

if __name__ == '__main__':
    unittest.main()