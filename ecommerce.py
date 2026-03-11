def calcular_desconto(valor_compra, cupom=""):
    if valor_compra < 0:
        raise ValueError("O valor da compra não pode ser negativo.")

    desconto = 0
    if cupom == "QUERO20":
        desconto = 0.20
    elif valor_compra >= 100:
        desconto = 0.10
        
    return valor_compra * (1 - desconto)