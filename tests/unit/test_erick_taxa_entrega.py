import pytest

from localeats_quality import calcular_taxa_entrega


def test_erick_retorna_taxa_fixa_para_distancia_ate_tres_km():
    resultado = calcular_taxa_entrega(2.5)

    assert resultado == 5.00


def test_erick_retorna_taxa_fixa_no_limite_de_tres_km():
    resultado = calcular_taxa_entrega(3.0)

    assert resultado == 5.00


def test_erick_calcula_taxa_proporcional_para_distancia_acima_do_limite():
    resultado = calcular_taxa_entrega(5.0)

    assert resultado == 9.00


def test_erick_lanca_erro_para_distancia_zero():
    with pytest.raises(ValueError, match="Distancia deve ser maior que zero"):
        calcular_taxa_entrega(0)
