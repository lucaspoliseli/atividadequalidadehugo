import unittest
from ecommerce import calcular_desconto 

class TestQualidade(unittest.TestCase):

    def test_regra_100_reais(self):
        # TESTE VERDE: 100 reais deve resultar em 90
        # Com a nova regra de frete, 90 + 15 = 105
        self.assertEqual(calcular_desconto(100), 105.0)

    def test_cupom_especial(self):
        # TESTE VERDE: Cupom QUERO20 em compra de 50 deve resultar em 40
        # Com a nova regra de frete, 40 + 15 = 55
        self.assertEqual(calcular_desconto(50, "QUERO20"), 55.0)

    def test_cenario_frete_pequena_compra(self):
        # Cenário de Frete:
        # Compra de 100 deve resultar em 90 (10% de desconto) + 15 de frete = 105
        self.assertEqual(calcular_desconto(100), 105.0)

    def test_cupom_valido_off50(self):
        # Cenário de Cupom Válido:
        # Compra de 800 com OFF50 => 400, sem frete (>= 150)
        self.assertEqual(calcular_desconto(800, "OFF50"), 400.0)

    def test_cupom_invalido_off50(self):
        # Cenário de Cupom Inválido:
        # Compra de 200 com OFF50 deve ignorar o cupom e aplicar 10% padrão
        # 200 - 10% = 180, sem frete (>= 150)
        self.assertEqual(calcular_desconto(200, "OFF50"), 180.0)

if __name__ == '__main__':
    unittest.main()