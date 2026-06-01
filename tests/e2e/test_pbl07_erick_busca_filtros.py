import pytest
from playwright.sync_api import Page, expect

from tests.e2e.pages.local_eats_page import LocalEatsPage


@pytest.mark.e2e
def test_erick_filtro_por_categoria_japonesa_atualiza_lista(page: Page):
    local_eats = LocalEatsPage(page)
    local_eats.preparar_usuario_autenticado()
    local_eats.acessar_inicio()

    local_eats.filtrar_categoria("Japonesa")

    expect(page.locator(".filter-btn.active")).to_contain_text("Japonesa")
    expect(local_eats.cards_restaurantes().first).to_be_visible(timeout=15000)
    expect(local_eats.cards_restaurantes().first).to_contain_text("Japonesa")


@pytest.mark.e2e
def test_erick_busca_por_regiao_centro_retorna_resultados(page: Page):
    local_eats = LocalEatsPage(page)
    local_eats.preparar_usuario_autenticado()
    local_eats.acessar_inicio()

    local_eats.buscar_por_termo("Centro")

    expect(local_eats.cards_restaurantes().first).to_be_visible(timeout=15000)
    expect(local_eats.cards_restaurantes().first).to_contain_text("Centro")
