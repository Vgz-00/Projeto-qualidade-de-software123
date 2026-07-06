# Aula 17 - Integracao Continua, Qualidade Automatizada, Metricas e Gestao de Defeitos

*Disciplina:* Qualidade de Software  
*Projeto:* LocalEats  
*Integrantes do grupo:*

* Vinicius Ortiz
* Augusto Martins
* Erick Rodrigues

---

## 1. Objetivo

Demonstrar um fluxo de qualidade automatizado usando versionamento, testes automatizados, GitHub Actions, indicadores de qualidade e registro de defeitos. A funcionalidade escolhida foi a validacao automatizada da regra de taxa de entrega.

---

## 2. Divisao por Integrante

| Integrante | Responsabilidade |
|---|---|
| Vinicius Ortiz | Estrutura do repositorio e workflow de CI |
| Augusto Martins | Registro de defeito e analise de severidade |
| Erick Rodrigues | Teste automatizado, metricas e documentacao da funcionalidade |

---

## 3. Repositorio da Atividade

| Item | Descricao |
|---|---|
| Nome do repositorio | `Projeto-qualidade-de-software123` |
| Link do repositorio | https://github.com/Vgz-00/Projeto-qualidade-de-software123 |

### Estrutura de diretorios utilizada

```text
Projeto-qualidade-de-software123/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── quality.yml
├── docs/
│   ├── issues/
│   │   ├── pbl12-defeito-distancia-invalida.md
│   │   └── pbl12-funcionalidade-quality-gate.md
│   ├── metricas/
│   │   └── pbl12-indicadores-qualidade.md
│   └── atividade-12PBL-aula17-integracao-continua-qualidade.md
├── src/
│   └── localeats_quality/
│       └── regras_pedido.py
├── tests/
│   ├── ci/
│   │   └── test_pbl12_taxa_entrega_quality_gate.py
│   └── unit/
│       └── test_erick_taxa_entrega.py
├── pytest.ini
└── requirements.txt
```

---

## 4. Planejamento da Funcionalidade

| Item | Descricao |
|---|---|
| Titulo da Issue | `[PBL 12] Validar regra de taxa de entrega no pipeline de qualidade` |
| Objetivo da funcionalidade | Garantir que a regra de taxa de entrega seja validada automaticamente no CI |
| Link da Issue | `docs/issues/pbl12-funcionalidade-quality-gate.md` |

### Criterios de aceite

* Taxa fixa para entregas ate 3 km.
* Taxa proporcional para entregas acima de 3 km.
* Distancias invalidas devem gerar erro.
* O pipeline deve executar os testes automaticamente em push e pull request.

---

## 5. Teste Automatizado

| Item | Descricao |
|---|---|
| Tipo de teste | Unitario / Quality Gate |
| Objetivo do teste | Validar a regra de taxa de entrega no pipeline de CI |
| Link para o arquivo do teste | `tests/ci/test_pbl12_taxa_entrega_quality_gate.py` |

Codigo do teste:

```python
import pytest

from localeats_quality import calcular_taxa_entrega


def test_quality_gate_taxa_fixa_para_entrega_curta():
    assert calcular_taxa_entrega(1.5) == 5.00


def test_quality_gate_taxa_proporcional_para_entrega_longa():
    assert calcular_taxa_entrega(6.0) == 11.00


def test_quality_gate_rejeita_distancia_invalida():
    with pytest.raises(ValueError, match="Distancia deve ser maior que zero"):
        calcular_taxa_entrega(-1)
```

---

## 6. Pipeline de Integracao Continua

| Item | Descricao |
|---|---|
| Nome do workflow | LocalEats Quality Gate |
| Evento que dispara a execucao | `push` e `pull_request` para a branch `main` |
| Link para o arquivo do workflow | `.github/workflows/quality.yml` |
| Link de uma execucao do workflow | https://github.com/Vgz-00/Projeto-qualidade-de-software123/actions/runs/28829839579 |

Codigo do workflow:

```yaml
name: LocalEats Quality Gate

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  tests:
    name: Automated quality checks
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run unit and CI tests
        run: python -m pytest tests/unit tests/ci -q
```

---

## 7. Indicadores de Qualidade

Indicadores gerados localmente antes do envio ao GitHub:

| Indicador | Valor |
|---|---:|
| Quantidade de testes executados | 15 |
| Quantidade de testes aprovados | 15 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline local | Aprovado |
| Status final do GitHub Actions | Aprovado |

Comando:

```bash
python -m pytest tests/unit tests/ci -q
```

Resultado:

```text
...............                                                          [100%]
15 passed
```

Execucao no GitHub Actions:

```text
LocalEats Quality Gate - success
Run: https://github.com/Vgz-00/Projeto-qualidade-de-software123/actions/runs/28829839579
```

---

## 8. Registro de Defeito

| Item | Descricao |
|---|---|
| Titulo do defeito | `[Bug] Taxa de entrega aceitava distancia invalida` |
| Severidade | Media |
| Link da Issue | `docs/issues/pbl12-defeito-distancia-invalida.md` |

**Qual foi o defeito?**  
Foi simulado um defeito em que a regra de taxa de entrega aceitava distancia menor ou igual a zero.

**Como ele foi identificado?**  
Foi identificado por teste automatizado usando a entrada `-1` km.

**Como foi corrigido?**  
A funcao passou a validar a distancia e lancar `ValueError` para entradas invalidas. O teste de quality gate garante que o erro nao volte.

---

## 9. Observacao sobre Issues

Foram adicionados templates de Issue em `.github/ISSUE_TEMPLATE/` e registros versionados em `docs/issues/`. Os registros em Markdown representam as Issues planejadas para a atividade e mantem a evidencia rastreavel no proprio repositorio. Caso necessario, a equipe pode criar as duas Issues reais pelo GitHub usando os textos ja prontos nesses arquivos.

---

## 10. Conclusao

O PBL 12 demonstrou um fluxo de qualidade automatizado: funcionalidade planejada, teste automatizado, pipeline de CI, metricas e registro de defeito. Esse fluxo reduz a chance de regressao e cria evidencias objetivas para acompanhar a qualidade do projeto.
