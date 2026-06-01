"""Regras de negocio simuladas para os PBLs de Qualidade de Software."""

from .regras_pedido import (
    aplicar_desconto_percentual,
    calcular_taxa_entrega,
    calcular_total_pedido,
)

__all__ = [
    "aplicar_desconto_percentual",
    "calcular_taxa_entrega",
    "calcular_total_pedido",
]
