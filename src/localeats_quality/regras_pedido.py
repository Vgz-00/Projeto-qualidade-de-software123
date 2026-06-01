"""Regras de negocio usadas nos testes unitarios do LocalEats."""

from __future__ import annotations


def calcular_total_pedido(itens: list[dict], valor_minimo: float) -> float:
    """Soma itens do pedido e valida se o valor minimo foi atingido."""
    if valor_minimo < 0:
        raise ValueError("Valor minimo nao pode ser negativo.")

    if not itens:
        raise ValueError("Pedido deve possuir ao menos um item.")

    total = 0.0

    for item in itens:
        preco = float(item.get("preco", 0))
        quantidade = int(item.get("quantidade", 1))

        if preco <= 0:
            raise ValueError("Preco do item deve ser maior que zero.")
        if quantidade <= 0:
            raise ValueError("Quantidade do item deve ser maior que zero.")

        total += preco * quantidade

    total = round(total, 2)

    if total < valor_minimo:
        raise ValueError("Valor minimo do pedido nao atingido.")

    return total


def aplicar_desconto_percentual(valor_total: float, percentual_desconto: float) -> float:
    """Aplica desconto percentual mantendo o valor final valido."""
    if valor_total < 0:
        raise ValueError("Valor total nao pode ser negativo.")

    if percentual_desconto < 0 or percentual_desconto > 100:
        raise ValueError("Percentual de desconto deve estar entre 0 e 100.")

    valor_com_desconto = valor_total * (1 - percentual_desconto / 100)
    return round(valor_com_desconto, 2)


def calcular_taxa_entrega(distancia_km: float) -> float:
    """Calcula taxa de entrega a partir da distancia informada."""
    if distancia_km <= 0:
        raise ValueError("Distancia deve ser maior que zero.")

    taxa_fixa = 5.00
    limite_taxa_fixa = 3.0
    taxa_por_km_excedente = 2.00

    if distancia_km <= limite_taxa_fixa:
        return taxa_fixa

    km_excedentes = distancia_km - limite_taxa_fixa
    return round(taxa_fixa + km_excedentes * taxa_por_km_excedente, 2)
