# Aula 9 - Testes Unitarios Automatizados e TDD

*Disciplina:* Qualidade de Software  
*Projeto:* LocalEats  
*Integrantes do grupo:*

* Vinicius Ortiz
* Augusto Martins
* Erick Rodrigues

---

## 1. Objetivo

Aplicar testes unitarios automatizados e o ciclo TDD em regras de negocio do sistema LocalEats. Como o sistema original nao disponibiliza seu codigo-fonte completo para alteracao direta, foram criadas funcoes simuladas em Python seguindo regras reais do dominio de pedidos.

Arquivos criados:

* `src/localeats_quality/regras_pedido.py`
* `tests/unit/test_vinicius_total_pedido.py`
* `tests/unit/test_augusto_desconto_percentual.py`
* `tests/unit/test_erick_taxa_entrega.py`

---

## 2. Divisao por Integrante

| Integrante | Regra de negocio | Arquivo de teste |
| ---------- | ---------------- | ---------------- |
| Vinicius Ortiz | Calculo do total do pedido com valor minimo | `tests/unit/test_vinicius_total_pedido.py` |
| Augusto Martins | Aplicacao de desconto percentual | `tests/unit/test_augusto_desconto_percentual.py` |
| Erick Rodrigues | Calculo de taxa de entrega | `tests/unit/test_erick_taxa_entrega.py` |

---

## 3. Funcionalidades Escolhidas

### 3.1 Vinicius Ortiz - Calculo do total do pedido

**O que faz:** soma os itens do pedido e verifica se o valor minimo exigido pelo restaurante foi atingido.

**Importancia:** evita que pedidos abaixo do minimo sejam aceitos, protegendo a regra comercial do restaurante.

**Regras de negocio:**

* O total e calculado por `preco * quantidade`
* O pedido deve possuir ao menos um item
* O valor minimo nao pode ser negativo
* Se o total for menor que o valor minimo, o sistema deve gerar erro

**Testes criados:**

| Teste | Resultado esperado |
| ----- | ------------------ |
| Total com valor minimo atingido | Retorna o total do pedido |
| Total considerando quantidade | Multiplica preco por quantidade |
| Total abaixo do minimo | Lanca `ValueError` |
| Pedido sem itens | Lanca `ValueError` |

---

### 3.2 Augusto Martins - Aplicacao de desconto percentual

**O que faz:** aplica um desconto percentual sobre o valor total do pedido.

**Importancia:** a regra impacta diretamente o preco final e evita descontos invalidos em promocoes.

**Regras de negocio:**

* Percentual deve estar entre 0% e 100%
* Valor total nao pode ser negativo
* Desconto de 0% mantem o valor original
* Desconto de 100% resulta em valor final zero

**Testes criados:**

| Teste | Resultado esperado |
| ----- | ------------------ |
| Desconto de 10% | Retorna valor com desconto |
| Desconto de 0% | Mantem valor original |
| Desconto de 100% | Retorna zero |
| Desconto acima de 100% | Lanca `ValueError` |

---

### 3.3 Erick Rodrigues - Calculo de taxa de entrega

**O que faz:** calcula a taxa de entrega com base na distancia em quilometros.

**Importancia:** padroniza a cobranca de entrega e evita valores incorretos para o cliente.

**Regras de negocio:**

* Distancia menor ou igual a 3 km usa taxa fixa de R$ 5,00
* Distancia acima de 3 km usa R$ 5,00 + R$ 2,00 por km excedente
* Distancia menor ou igual a zero e invalida

**Testes criados:**

| Teste | Resultado esperado |
| ----- | ------------------ |
| Distancia ate 3 km | Retorna R$ 5,00 |
| Distancia exatamente 3 km | Retorna R$ 5,00 |
| Distancia acima de 3 km | Retorna taxa proporcional |
| Distancia zero | Lanca `ValueError` |

---

## 4. Aplicacao do TDD

O ciclo TDD foi aplicado seguindo as etapas:

1. **Red:** primeiro foram definidos os testes com o comportamento esperado.
2. **Green:** depois foram implementadas as funcoes minimas para fazer os testes passarem.
3. **Refactor:** por fim, o codigo foi organizado com nomes claros, validacoes separadas por regra e arredondamento de valores monetarios.

Exemplo do ciclo aplicado na regra de taxa de entrega:

```python
def test_erick_calcula_taxa_proporcional_para_distancia_acima_do_limite():
    resultado = calcular_taxa_entrega(5.0)

    assert resultado == 9.00
```

Implementacao final:

```python
def calcular_taxa_entrega(distancia_km: float) -> float:
    if distancia_km <= 0:
        raise ValueError("Distancia deve ser maior que zero.")

    taxa_fixa = 5.00
    limite_taxa_fixa = 3.0
    taxa_por_km_excedente = 2.00

    if distancia_km <= limite_taxa_fixa:
        return taxa_fixa

    km_excedentes = distancia_km - limite_taxa_fixa
    return round(taxa_fixa + km_excedentes * taxa_por_km_excedente, 2)
```

---

## 5. Execucao dos Testes

Comando utilizado:

```bash
python -m pytest tests/unit -q
```

Resultado obtido:

```text
............                                                             [100%]
12 passed in 0.15s
```

---

## 6. Reflexao

O TDD ajudou a transformar regras de negocio em comportamentos verificaveis. Antes de pensar na implementacao, a equipe precisou definir entradas, saidas e cenarios de erro. Isso tornou o codigo mais simples de manter e reduziu a chance de aceitar regras invalidas, como pedido abaixo do minimo, desconto acima de 100% ou distancia de entrega igual a zero.

Como melhoria futura, os testes poderiam ser parametrizados com `pytest.mark.parametrize` para cobrir mais valores com menos repeticao.

