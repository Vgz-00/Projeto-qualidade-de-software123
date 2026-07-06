# Issue de Defeito - PBL 12

## Titulo

[Bug] Taxa de entrega aceitava distancia invalida

## Severidade

Media

## Defeito

Foi simulado um defeito em que a regra de taxa de entrega poderia aceitar distancia menor ou igual a zero, permitindo uma cobranca sem sentido para o usuario.

## Como foi identificado

O defeito foi identificado por teste automatizado de quality gate com entrada `-1` km.

## Como foi corrigido

A funcao `calcular_taxa_entrega` valida a entrada e lanca `ValueError` quando a distancia e menor ou igual a zero. O teste `test_quality_gate_rejeita_distancia_invalida` garante que a correcao nao regrida.

## Responsavel

Augusto Martins
