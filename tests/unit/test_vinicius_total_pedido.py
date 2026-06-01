import pytest

from localeats_quality import calcular_total_pedido


def test_vinicius_calcula_total_quando_valor_minimo_atingido():
    itens = [{"preco": 18.90}, {"preco": 12.10}]

    resultado = calcular_total_pedido(itens, valor_minimo=25.00)

    assert resultado == 31.00


def test_vinicius_calcula_total_com_quantidade_de_itens():
    itens = [{"preco": 10.00, "quantidade": 2}, {"preco": 7.50, "quantidade": 1}]

    resultado = calcular_total_pedido(itens, valor_minimo=20.00)

    assert resultado == 27.50


def test_vinicius_lanca_erro_quando_valor_minimo_nao_e_atingido():
    itens = [{"preco": 8.00}, {"preco": 4.50}]

    with pytest.raises(ValueError, match="Valor minimo do pedido nao atingido"):
        calcular_total_pedido(itens, valor_minimo=20.00)


def test_vinicius_lanca_erro_para_pedido_sem_itens():
    with pytest.raises(ValueError, match="Pedido deve possuir ao menos um item"):
        calcular_total_pedido([], valor_minimo=15.00)
