# Indicadores de Qualidade - PBL 12

| Indicador | Valor |
|---|---:|
| Quantidade de testes unitarios executados | 12 |
| Quantidade de testes de quality gate executados | 3 |
| Total de testes executados no recorte de CI | 15 |
| Quantidade de testes aprovados | 15 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline local | Aprovado |
| Status final do GitHub Actions | Aprovado |

Comando usado para gerar os indicadores:

```bash
python -m pytest tests/unit tests/ci -q
```

Resultado local:

```text
...............                                                          [100%]
15 passed
```

Execucao do workflow:

https://github.com/Vgz-00/Projeto-qualidade-de-software123/actions/runs/28829839579
