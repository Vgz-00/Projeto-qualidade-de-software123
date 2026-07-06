# Aula 15 - Modelos de Maturidade

*Disciplina:* Qualidade de Software  
*Projeto:* LocalEats  
*Integrantes do grupo:*

* Vinicius Ortiz
* Augusto Martins
* Erick Rodrigues

---

## 1. Objetivo

Avaliar a maturidade do processo utilizado pela equipe no projeto LocalEats, considerando praticas relacionadas a CMMI, MPS.BR, organizacao de artefatos, controle de qualidade e melhoria continua.

---

## 2. Divisao por Integrante

| Integrante | Responsabilidade |
|---|---|
| Vinicius Ortiz | Diagnostico de maturidade |
| Augusto Martins | Identificacao das lacunas do processo |
| Erick Rodrigues | Propostas de melhoria e classificacao final |

---

## 3. Diagnostico de Maturidade

| Criterio | Sim | Parcial | Nao | Justificativa |
|---|:---:|:---:|:---:|---|
| Os requisitos sao documentados? |  | X |  | Os requisitos aparecem nos enunciados dos PBLs e nos documentos, mas ainda nao ha backlog padronizado. |
| Existe controle de mudancas? |  | X |  | O Git registra commits, mas mudancas ainda nao sao formalizadas por Issue em todos os casos. |
| Ha atividades de teste definidas? | X |  |  | Existem testes unitarios, E2E, BDD e testes de CI criados no repositorio. |
| Os defeitos sao registrados? |  | X |  | Alguns defeitos sao descritos nos documentos; o registro por Issue ainda precisa ser mais constante. |
| O processo de desenvolvimento e conhecido por toda a equipe? |  | X |  | O fluxo e compreendido, mas nao estava formalmente documentado antes do PBL 9. |
| As tarefas sao planejadas e acompanhadas regularmente? |  | X |  | Ha divisao por integrante, mas ainda falta quadro visual ou acompanhamento sistematico. |
| Existe padronizacao para implementacao de funcionalidades? |  | X |  | Existe padrao nos testes Python, mas ainda pode haver checklists de codigo e revisao. |
| Os testes sao executados antes da entrega das funcionalidades? | X |  |  | Nos PBLs recentes, os testes foram executados antes do commit e da publicacao. |
| Ha revisao de codigo ou validacao por outro integrante? |  | X |  | A revisao existe de forma informal; precisa ser formalizada em pull requests ou checklist. |
| A equipe utiliza ferramentas para gerenciamento das atividades? |  | X |  | O GitHub e usado para versionamento, mas Issues/Projects ainda nao sao usados plenamente. |
| Os artefatos do projeto sao organizados e versionados? | X |  |  | Documentos, testes, features e workflows estao no repositorio. |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? |  | X |  | Os documentos citam as atividades, mas ainda faltam links entre Issue, commit, teste e requisito. |
| A equipe realiza retrospectivas para identificar melhorias? |  | X |  | As reflexoes existem nos PBLs, mas poderiam virar ritual fixo. |
| Existem indicadores ou metricas para acompanhar a qualidade do projeto? |  | X |  | O PBL 12 iniciou metricas de testes, mas ainda nao ha acompanhamento historico. |

---

## 4. Classificacao do Processo

**Classificacao escolhida:** Gerenciado.

O processo ja possui organizacao minima, responsabilidades por integrante, versionamento no GitHub e testes automatizados. Isso mostra que a equipe nao esta mais em um nivel totalmente inicial. Mesmo assim, ainda faltam padronizacao forte, rastreabilidade completa, uso constante de Issues, metricas historicas e melhoria continua formal. Por isso, o nivel mais coerente e **Gerenciado**, com evolucao possivel para **Definido**.

---

## 5. Lacunas Identificadas

| Lacuna | Impacto |
|---|---|
| Uso pouco consistente de Issues | Dificulta rastrear demandas, defeitos e responsaveis |
| Ausencia de metricas historicas | A equipe sabe se os testes passaram, mas nao acompanha tendencia de qualidade |
| Revisao informal dos artefatos | Pode permitir erros de documentacao, criterios ausentes ou testes incompletos |
| Falta de Definition of Ready e Definition of Done | Funcionalidades podem iniciar ou terminar sem criterios objetivos |
| Rastreabilidade parcial | Nem sempre e possivel ligar requisito, teste, commit e evidencia |

---

## 6. Propostas de Melhoria

| Melhoria | Beneficio |
|---|---|
| Criar Issues para cada PBL, funcionalidade ou defeito | Melhora rastreabilidade e acompanhamento |
| Adotar checklist de revisao antes da entrega | Reduz esquecimentos e aumenta consistencia |
| Manter GitHub Actions executando testes automatizados | Garante validacao automatica a cada mudanca |
| Registrar metricas por entrega | Permite acompanhar evolucao da qualidade |
| Definir DoR e DoD para atividades | Torna claro quando uma tarefa pode iniciar e quando esta concluida |

---

## 7. Conclusao

A equipe apresenta maturidade intermediaria. Ha boas praticas em evolucao, como testes automatizados e versionamento, mas o processo ainda depende de organizacao manual e revisoes informais. Com Issues, metricas, DoR, DoD e CI, o processo pode evoluir para um nivel mais definido e previsivel.

