# Issue de Funcionalidade - PBL 12

## Titulo

[PBL 12] Validar regra de taxa de entrega no pipeline de qualidade

## Objetivo da funcionalidade

Garantir que a regra de taxa de entrega do LocalEats seja validada automaticamente no fluxo de integracao continua.

## Criterios de aceite

- A regra deve retornar taxa fixa para distancias ate 3 km.
- A regra deve retornar taxa proporcional para distancias acima de 3 km.
- A regra deve rejeitar distancia menor ou igual a zero.
- O workflow do GitHub Actions deve executar os testes em push e pull request.

## Responsavel

Erick Rodrigues

## Observacao

Este arquivo registra a Issue planejada para a atividade. O ambiente do Codex nao possui permissao para criar Issues reais neste repositorio via API, entao o registro foi versionado no proprio repositorio.
