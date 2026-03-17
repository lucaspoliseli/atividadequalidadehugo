import unittest
from ecommerce import calcular_desconto 

class TestQualidade(unittest.TestCase):

    def test_regra_100_reais(self):
        self.assertEqual(calcular_desconto(100), 105.0)

    def test_cupom_especial(self):
        self.assertEqual(calcular_desconto(50, "QUERO20"), 55.0)

    def test_cenario_frete_pequena_compra(self):
        self.assertEqual(calcular_desconto(100), 105.0)

    def test_cupom_valido_off50(self):
        self.assertEqual(calcular_desconto(800, "OFF50"), 400.0)

    def test_cupom_invalido_off50(self):
        self.assertEqual(calcular_desconto(200, "OFF50"), 180.0)

if __name__ == '__main__':
    unittest.main()