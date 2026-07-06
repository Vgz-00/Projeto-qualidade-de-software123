# Aula 16 - Qualidade em Metodologias Ageis

*Disciplina:* Qualidade de Software  
*Projeto:* LocalEats  
*Integrantes do grupo:*

* Vinicius Ortiz
* Augusto Martins
* Erick Rodrigues

---

## 1. Objetivo

Analisar o processo da equipe sob a perspectiva de metodologias ageis e propor melhorias que aumentem colaboracao, visibilidade, previsibilidade e qualidade nas entregas do LocalEats.

---

## 2. Divisao por Integrante

| Integrante | Responsabilidade |
|---|---|
| Vinicius Ortiz | Analise das praticas ageis |
| Augusto Martins | Propostas de melhoria e Definition of Ready |
| Erick Rodrigues | Definition of Done e conclusao |

---

## 3. Analise de Praticas Ageis no Processo

| Pratica | Existe no processo? | Como e aplicada atualmente? | Pode ser melhorada? |
|---|---|---|---|
| Planejamento iterativo | Parcial | A equipe trabalha por PBL, cada um com objetivo especifico. | Sim, definindo mini-sprints para leitura, execucao, revisao e entrega. |
| Priorizacao de funcionalidades | Parcial | As prioridades seguem o que o enunciado exige primeiro. | Sim, priorizando itens por risco e impacto na avaliacao. |
| Entregas incrementais | Sim | Cada PBL adiciona novos documentos, testes ou artefatos ao repositorio. | Sim, usando commits menores e mais frequentes. |
| Feedback frequente | Parcial | O feedback ocorre na revisao e nas reflexoes das atividades. | Sim, com revisoes curtas antes do commit final. |
| Trabalho colaborativo | Sim | As entregas sao divididas entre Vinicius, Augusto e Erick. | Sim, com pareamento em partes mais tecnicas. |
| Controle visual das atividades | Parcial | O GitHub mostra arquivos e commits, mas nao ha quadro de tarefas constante. | Sim, usando GitHub Projects ou quadro Kanban. |
| Melhoria continua | Parcial | Cada PBL inclui reflexoes e melhorias propostas. | Sim, transformando melhorias em acoes rastreaveis por Issue. |

### Conclusao da Analise

O processo da equipe ja possui caracteristicas ageis, principalmente entregas incrementais e divisao colaborativa. Entretanto, ainda falta transformar essas praticas em rotina visivel e controlada. O uso de Kanban, DoR, DoD, retrospectivas e CI ajudaria a equipe a manter velocidade sem perder qualidade.

---

## 4. Propostas de Melhoria Agil

| Melhoria Proposta | Metodologia Relacionada | Beneficio Esperado |
|---|---|---|
| Criar um quadro Kanban com colunas A Fazer, Em Andamento, Revisao e Concluido | Kanban | Aumenta visibilidade e reduz tarefas esquecidas |
| Definir uma Definition of Ready antes de iniciar cada PBL | Scrum | Evita comecar atividades sem entendimento suficiente |
| Definir uma Definition of Done para cada entrega | Scrum / XP | Garante que documento, teste e evidencia estejam completos |
| Executar testes automatizados antes de cada commit final | XP / CI | Reduz regressao e aumenta confianca |
| Realizar retrospectiva curta apos cada PBL | Scrum / Lean | Ajuda a identificar melhorias reais no processo |
| Limitar trabalho em progresso | Kanban / Lean | Evita muitas tarefas abertas ao mesmo tempo |

---

## 5. Definition of Ready (DoR)

Uma funcionalidade ou atividade esta pronta para entrar em desenvolvimento quando:

1. O enunciado do PBL foi lido e entendido pela equipe.
2. Os criterios obrigatorios de entrega foram identificados.
3. A responsabilidade de cada integrante foi definida.
4. Os arquivos ou artefatos esperados foram listados.
5. Os riscos principais foram identificados, como dependencia de API, CI ou ferramenta externa.
6. Existe uma ideia clara de como a entrega sera validada.
7. Quando houver codigo, o ambiente minimo de execucao foi definido.

---

## 6. Definition of Done (DoD)

Uma funcionalidade ou atividade e considerada concluida quando:

1. Todos os itens obrigatorios do enunciado foram atendidos.
2. O documento Markdown foi criado no repositorio.
3. Os arquivos de codigo, teste ou evidencia foram versionados quando aplicavel.
4. Os testes automatizados relevantes foram executados com sucesso.
5. A entrega possui divisao clara por integrante.
6. O README ou estrutura do repositorio esta coerente com os novos arquivos.
7. O commit foi enviado ao GitHub.
8. O link do repositorio esta pronto para ser entregue ao professor.

---

## 7. Conclusao

As metodologias ageis podem melhorar o processo da equipe sem deixar a qualidade de lado. O ponto mais importante e transformar praticas informais em criterios objetivos. Com Kanban, DoR, DoD, revisao e testes automatizados, a equipe consegue entregar de forma mais organizada, rastreavel e confiavel.

