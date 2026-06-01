import pytest
from playwright.sync_api import Page, expect

from tests.e2e.pages.local_eats_page import LocalEatsPage


@pytest.mark.e2e
def test_augusto_detalhes_exibem_cardapio_do_restaurante(page: Page):
    local_eats = LocalEatsPage(page)
    local_eats.preparar_usuario_autenticado()
    local_eats.acessar_inicio()

    local_eats.abrir_primeiro_restaurante()

    expect(page.locator("#restName")).to_be_visible()
    expect(page.locator("#menuList .menu-item").first).to_be_visible(timeout=15000)


@pytest.mark.e2e
def test_augusto_aba_avaliacoes_exibe_conteudo(page: Page):
    local_eats = LocalEatsPage(page)
    local_eats.preparar_usuario_autenticado()
    local_eats.acessar_inicio()
    local_eats.abrir_primeiro_restaurante()

    page.get_by_role("button", name="Avaliações").click()

    expect(page.locator("#reviewsTab.active")).to_be_visible()
    expect(page.locator("#reviewList")).to_be_visible()
