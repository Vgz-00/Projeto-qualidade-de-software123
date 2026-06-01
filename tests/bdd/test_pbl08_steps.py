from __future__ import annotations

import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then, when

from tests.e2e.pages.local_eats_page import LocalEatsPage


FEATURES_DIR = Path(__file__).resolve().parents[2] / "features"

scenarios(str(FEATURES_DIR / "erick_busca_restaurantes.feature"))
scenarios(str(FEATURES_DIR / "vinicius_visualizacao_restaurantes.feature"))
scenarios(str(FEATURES_DIR / "augusto_navegacao_paginas.feature"))


@pytest.fixture
def local_eats(page: Page):
    app = LocalEatsPage(page)
    app.preparar_usuario_autenticado()
    return app


@given("que o usuario esta autenticado na pagina inicial")
def usuario_na_pagina_inicial(local_eats: LocalEatsPage):
    local_eats.acessar_inicio()


@when(parsers.parse('o usuario busca pela regiao "{regiao}"'))
def buscar_por_regiao(local_eats: LocalEatsPage, regiao: str):
    local_eats.buscar_por_termo(regiao)


@when("o usuario executa uma busca vazia")
def busca_vazia(local_eats: LocalEatsPage):
    local_eats.buscar_por_termo("")


@when(parsers.parse('o usuario acessa a pagina "{pagina}"'))
def acessar_pagina(local_eats: LocalEatsPage, pagina: str):
    if pagina == "Meus Favoritos":
        local_eats.acessar_favoritos()
        return

    if pagina == "Meus Pedidos":
        local_eats.acessar_pedidos()
        return

    raise AssertionError(f"Pagina nao suportada no teste: {pagina}")


@then(parsers.parse('a lista deve exibir restaurantes da regiao "{regiao}"'))
def lista_exibe_regiao(local_eats: LocalEatsPage, regiao: str):
    expect(local_eats.cards_restaurantes().first).to_be_visible(timeout=15000)
    expect(local_eats.cards_restaurantes().first).to_contain_text(regiao)


@then("a lista de restaurantes deve continuar visivel")
def lista_continua_visivel(local_eats: LocalEatsPage):
    expect(local_eats.cards_restaurantes().first).to_be_visible(timeout=15000)


@then("pelo menos um card de restaurante deve aparecer")
def card_restaurante_aparece(local_eats: LocalEatsPage):
    expect(local_eats.cards_restaurantes().first).to_be_visible(timeout=15000)


@then("o primeiro restaurante deve exibir nome e imagem")
def card_exibe_nome_e_imagem(local_eats: LocalEatsPage):
    primeiro_card = local_eats.cards_restaurantes().first

    expect(primeiro_card.locator(".card-title")).to_contain_text("Restaurante")
    expect(primeiro_card.locator(".card-img")).to_have_attribute("src", re.compile(r"https?://"))


@then("a pagina de favoritos deve ser exibida")
def pagina_favoritos_exibida(local_eats: LocalEatsPage):
    expect(local_eats.page.get_by_text("Restaurantes Favoritos")).to_be_visible()


@then("o historico de pedidos deve ser exibido")
def historico_pedidos_exibido(local_eats: LocalEatsPage):
    expect(local_eats.page.get_by_text("Histórico de Transações")).to_be_visible()
