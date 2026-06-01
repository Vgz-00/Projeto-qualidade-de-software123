# Aula 10 - Testes Funcionais Automatizados

*Disciplina:* Qualidade de Software  
*Projeto:* LocalEats  
*Integrantes do grupo:*

* Vinicius Ortiz
* Augusto Martins
* Erick Rodrigues

---

## 1. Objetivo

Automatizar fluxos funcionais do sistema LocalEats utilizando Playwright com Pytest. Os testes foram organizados com Page Object Model para evitar repeticao de seletores e facilitar manutencao.

Arquivos criados:

* `tests/e2e/pages/local_eats_page.py`
* `tests/e2e/test_pbl07_vinicius_navegacao_restaurantes.py`
* `tests/e2e/test_pbl07_augusto_detalhes_restaurante.py`
* `tests/e2e/test_pbl07_erick_busca_filtros.py`

---

## 2. Divisao por Integrante

| Integrante | Fluxo funcional | Testes automatizados |
| ---------- | --------------- | -------------------- |
| Vinicius Ortiz | Navegacao e visualizacao de restaurantes | Lista carregada e clique em restaurante |
| Augusto Martins | Detalhes de restaurante | Cardapio e aba de avaliacoes |
| Erick Rodrigues | Busca e filtros | Filtro por categoria e busca por regiao |

---

## 3. Teste Automatizado com Codegen

O Codegen foi usado como ponto de partida para reconhecer a estrutura da interface:

```bash
playwright codegen https://local-eats-unisenac.vercel.app/static/index.html
```

O Codegen ajudou a identificar elementos reais da pagina, como:

* Campo de busca: `#searchInput`
* Botao de busca: `#searchBtn`
* Botoes de filtro: `.filter-btn`
* Cards de restaurante: `.rest-card`

O codigo gerado pelo Codegen nao foi entregue diretamente, pois ele tende a ficar muito preso a cliques gravados. A equipe refatorou a automacao para Pytest e Page Object Model.

---

## 4. Page Object Model

Foi criada a classe `LocalEatsPage`, responsavel por centralizar acoes e seletores:

```python
class LocalEatsPage:
    def acessar_inicio(self) -> None:
        self.page.goto(f"{BASE_URL}/index.html")
        self.aguardar_lista_restaurantes()

    def cards_restaurantes(self):
        return self.page.locator(".rest-card")

    def filtrar_categoria(self, categoria: str) -> None:
        self.page.get_by_role("button", name=categoria).click()
```

Tambem foi criada uma preparacao de usuario autenticado para evitar que o sistema redirecione para a tela de login durante os testes. A autenticacao foi simulada no navegador e o endpoint `/users/me` foi mockado, mantendo os testes focados nos fluxos funcionais.

---

## 5. Fluxos Testados

### 5.1 Vinicius Ortiz - Navegacao e visualizacao

**Cenarios:**

* A lista de restaurantes carrega corretamente
* O clique no primeiro restaurante abre a pagina de detalhes

**Importancia:** esse fluxo e a entrada principal do usuario no sistema. Se a lista nao carregar ou se o card nao abrir detalhes, o usuario nao consegue iniciar um pedido.

---

### 5.2 Augusto Martins - Detalhes do restaurante

**Cenarios:**

* A pagina de detalhes exibe nome e cardapio
* A aba "Avaliacoes" exibe conteudo ao ser clicada

**Importancia:** antes de comprar, o usuario precisa visualizar informacoes do restaurante, cardapio e avaliacoes.

---

### 5.3 Erick Rodrigues - Busca e filtros

**Cenarios:**

* O filtro "Japonesa" atualiza a lista
* A busca por "Centro" retorna restaurantes da regiao informada

**Importancia:** busca e filtros melhoram a descoberta de restaurantes e reduzem o esforco do usuario.

---

## 6. Execucao dos Testes

Comando utilizado:

```bash
python -m pytest tests/e2e -q
```

Resultado obtido:

```text
......                                                                   [100%]
6 passed in 19.75s
```

---

## 7. Analise Critica

Os testes ficaram mais confiaveis depois da refatoracao com Page Object Model. O principal cuidado foi nao usar seletores antigos: a versao atual do LocalEats utiliza `.rest-card`, nao `.restaurant-card`.

Os testes ainda dependem do site publicado e da API de restaurantes. Caso a API fique fora do ar, a automacao pode falhar mesmo sem erro no codigo de teste. Para uma evolucao futura, seria interessante adicionar uma camada de mocks para os restaurantes ou criar uma base controlada de teste.

---

## 8. Conclusao

A automacao funcional validou os principais fluxos de descoberta do LocalEats. A estrutura criada permite evoluir a suite com novos cenarios, como adicionar item ao carrinho e finalizar pedido.

