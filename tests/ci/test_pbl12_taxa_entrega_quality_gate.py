import pytest

from localeats_quality import calcular_taxa_entrega


def test_quality_gate_taxa_fixa_para_entrega_curta():
    assert calcular_taxa_entrega(1.5) == 5.00


def test_quality_gate_taxa_proporcional_para_entrega_longa():
    assert calcular_taxa_entrega(6.0) == 11.00


def test_quality_gate_rejeita_distancia_invalida():
    with pytest.raises(ValueError, match="Distancia deve ser maior que zero"):
        calcular_taxa_entrega(-1)
