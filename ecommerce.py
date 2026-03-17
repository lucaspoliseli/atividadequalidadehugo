def calcular_desconto(valor_compra, cupom=""):
    if valor_compra < 0:
        raise ValueError("O valor da compra não pode ser negativo.")

    desconto = 0

    # Regra do cupom de segurança OFF50:
    # - Só aplica 50% se valor_compra > 600
    # - Caso contrário, ignora o cupom e segue as regras padrão
    if cupom == "OFF50" and valor_compra > 600:
        desconto = 0.50
    else:
        if cupom == "QUERO20":
            desconto = 0.20
        elif valor_compra >= 100:
            desconto = 0.10

    valor_final = valor_compra * (1 - desconto)

    # Regra de frete fixo:
    # Se o valor final (pós-desconto) for menor que 150,
    # adicionar taxa de 15 reais ao total.
    if valor_final < 150:
        valor_final += 15

    return valor_final