import pytest

from localeats_quality import aplicar_desconto_percentual


def test_augusto_aplica_desconto_de_dez_por_cento():
    resultado = aplicar_desconto_percentual(valor_total=100.00, percentual_desconto=10)

    assert resultado == 90.00


def test_augusto_mantem_valor_original_quando_desconto_e_zero():
    resultado = aplicar_desconto_percentual(valor_total=59.90, percentual_desconto=0)

    assert resultado == 59.90


def test_augusto_permite_desconto_total_sem_valor_negativo():
    resultado = aplicar_desconto_percentual(valor_total=45.00, percentual_desconto=100)

    assert resultado == 0.00


def test_augusto_lanca_erro_para_percentual_acima_de_cem():
    with pytest.raises(ValueError, match="Percentual de desconto deve estar entre 0 e 100"):
        aplicar_desconto_percentual(valor_total=80.00, percentual_desconto=120)
