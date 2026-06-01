import pytest
from playwright.sync_api import Page, expect

from tests.e2e.pages.local_eats_page import LocalEatsPage


@pytest.mark.e2e
def test_vinicius_lista_de_restaurantes_carrega(page: Page):
    local_eats = LocalEatsPage(page)
    local_eats.preparar_usuario_autenticado()

    local_eats.acessar_inicio()

    expect(local_eats.cards_restaurantes().first).to_be_visible()
    expect(local_eats.cards_restaurantes().first.locator(".card-title")).to_contain_text(
        "Restaurante"
    )


@pytest.mark.e2e
def test_vinicius_clique_no_restaurante_abre_detalhes(page: Page):
    local_eats = LocalEatsPage(page)
    local_eats.preparar_usuario_autenticado()
    local_eats.acessar_inicio()

    local_eats.abrir_primeiro_restaurante()

    expect(page.locator("#restName")).to_be_visible()
    expect(page.locator("#menuList")).to_be_visible()
