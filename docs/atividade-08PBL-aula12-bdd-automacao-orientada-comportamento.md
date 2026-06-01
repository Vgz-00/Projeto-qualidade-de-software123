# Aula 12 - BDD e Automacao Orientada a Comportamento

*Disciplina:* Qualidade de Software  
*Projeto:* LocalEats  
*Integrantes do grupo:*

* Vinicius Ortiz
* Augusto Martins
* Erick Rodrigues

---

## 1. Objetivo

Transformar comportamentos esperados do LocalEats em cenarios BDD usando Gherkin e automatizar esses cenarios com `pytest-bdd` integrado ao Playwright.

Arquivos criados:

* `features/vinicius_visualizacao_restaurantes.feature`
* `features/augusto_navegacao_paginas.feature`
* `features/erick_busca_restaurantes.feature`
* `tests/bdd/test_pbl08_steps.py`

---

## 2. Divisao por Integrante

| Integrante | Comportamento escolhido | Cenarios criados |
| ---------- | ----------------------- | ---------------- |
| Vinicius Ortiz | Visualizacao de restaurantes | 2 cenarios |
| Augusto Martins | Navegacao entre paginas | 2 cenarios |
| Erick Rodrigues | Busca de restaurantes | 2 cenarios |

Todos os cenarios foram escritos em Gherkin e automatizados com `pytest-bdd`.

---

## 3. Cenarios BDD

### 3.1 Erick Rodrigues - Busca de restaurantes

Arquivo: `features/erick_busca_restaurantes.feature`

```gherkin
Feature: Busca de restaurantes
  Como usuario do LocalEats
  Quero buscar restaurantes por regiao
  Para encontrar opcoes de forma mais rapida

  Scenario: Busca valida retorna restaurantes da regiao informada
    Given que o usuario esta autenticado na pagina inicial
    When o usuario busca pela regiao "Centro"
    Then a lista deve exibir restaurantes da regiao "Centro"

  Scenario: Busca vazia mantem a listagem de restaurantes
    Given que o usuario esta autenticado na pagina inicial
    When o usuario executa uma busca vazia
    Then a lista de restaurantes deve continuar visivel
```

---

### 3.2 Vinicius Ortiz - Visualizacao de restaurantes

Arquivo: `features/vinicius_visualizacao_restaurantes.feature`

```gherkin
Feature: Visualizacao de restaurantes
  Como usuario do LocalEats
  Quero visualizar os restaurantes disponiveis
  Para escolher onde fazer meu pedido

  Scenario: Cards de restaurantes sao carregados
    Given que o usuario esta autenticado na pagina inicial
    Then pelo menos um card de restaurante deve aparecer

  Scenario: Card de restaurante exibe nome e imagem
    Given que o usuario esta autenticado na pagina inicial
    Then o primeiro restaurante deve exibir nome e imagem
```

---

### 3.3 Augusto Martins - Navegacao entre paginas

Arquivo: `features/augusto_navegacao_paginas.feature`

```gherkin
Feature: Navegacao entre paginas
  Como usuario autenticado
  Quero navegar pelas paginas principais
  Para acessar favoritos e pedidos sem erro

  Scenario: Usuario acessa a pagina de favoritos
    Given que o usuario esta autenticado na pagina inicial
    When o usuario acessa a pagina "Meus Favoritos"
    Then a pagina de favoritos deve ser exibida

  Scenario: Usuario acessa a pagina de pedidos
    Given que o usuario esta autenticado na pagina inicial
    When o usuario acessa a pagina "Meus Pedidos"
    Then o historico de pedidos deve ser exibido
```

---

## 4. Automacao com pytest-bdd

A automacao foi concentrada em `tests/bdd/test_pbl08_steps.py`.

Exemplo de step reutilizado:

```python
@given("que o usuario esta autenticado na pagina inicial")
def usuario_na_pagina_inicial(local_eats: LocalEatsPage):
    local_eats.acessar_inicio()
```

Exemplo de verificacao de comportamento:

```python
@then(parsers.parse('a lista deve exibir restaurantes da regiao "{regiao}"'))
def lista_exibe_regiao(local_eats: LocalEatsPage, regiao: str):
    expect(local_eats.cards_restaurantes().first).to_be_visible(timeout=15000)
    expect(local_eats.cards_restaurantes().first).to_contain_text(regiao)
```

O mesmo Page Object usado no PBL 7 foi reaproveitado para manter os testes BDD mais legiveis e evitar repeticao.

---

## 5. Execucao dos Testes

Comando utilizado:

```bash
python -m pytest tests/bdd -q
```

Resultado obtido:

```text
......                                                                   [100%]
6 passed in 8.90s
```

---

## 6. Analise

O BDD deixou os testes mais proximos da linguagem de negocio. Uma pessoa nao tecnica consegue entender os cenarios lendo os arquivos `.feature`, enquanto a equipe tecnica consegue manter a automacao nos steps Python.

A principal vantagem em relacao aos testes E2E comuns e que o comportamento esperado fica documentado em frases simples:

* Buscar por uma regiao deve retornar restaurantes daquela regiao
* A lista de restaurantes deve continuar visivel quando a busca estiver vazia
* As paginas principais devem abrir sem erro

---

## 7. Conclusao

Foram criados 6 cenarios BDD, sendo 2 por integrante, e todos foram automatizados com `pytest-bdd` e Playwright. A entrega atende ao objetivo de criar documentacao viva: os cenarios funcionam como especificacao do comportamento esperado e tambem como teste executavel.

