from __future__ import annotations

import os
import re

from playwright.sync_api import Page, expect


BASE_URL = os.getenv(
    "LOCALEATS_URL",
    "https://local-eats-unisenac.vercel.app/static",
)


class LocalEatsPage:
    def __init__(self, page: Page):
        self.page = page

    def preparar_usuario_autenticado(self) -> None:
        self.page.route("**/users/me", self._mock_usuario)
        self.page.route("**/orders/", self._mock_pedidos)
        self.page.add_init_script(
            """
            window.localStorage.setItem('userId', '1');
            window.localStorage.setItem('userName', 'Equipe Tech Quality');
            """
        )

    def acessar_inicio(self) -> None:
        self.page.goto(f"{BASE_URL}/index.html")
        self.aguardar_lista_restaurantes()

    def aguardar_lista_restaurantes(self) -> None:
        expect(self.cards_restaurantes().first).to_be_visible(timeout=15000)

    def cards_restaurantes(self):
        return self.page.locator(".rest-card")

    def primeiro_card(self):
        return self.cards_restaurantes().first

    def abrir_primeiro_restaurante(self) -> None:
        self.primeiro_card().click()
        expect(self.page).to_have_url(re.compile(r"restaurant\.html\?id=\d+"))
        expect(self.page.locator("#restaurantContent")).to_be_visible(timeout=15000)

    def buscar_por_termo(self, termo: str) -> None:
        self.page.locator("#searchInput").fill(termo)
        self.page.locator("#searchBtn").click()

    def filtrar_categoria(self, categoria: str) -> None:
        self.page.get_by_role("button", name=categoria).click()

    def acessar_favoritos(self) -> None:
        self.page.get_by_role("link", name="Meus Favoritos").click()
        expect(self.page).to_have_url(re.compile(r"profile\.html"))

    def acessar_pedidos(self) -> None:
        self.page.get_by_role("link", name="Meus Pedidos").click()
        expect(self.page).to_have_url(re.compile(r"orders\.html"))

    def _mock_usuario(self, route) -> None:
        route.fulfill(
            status=200,
            json={
                "id": 1,
                "name": "Equipe Tech Quality",
                "email": "techquality@localeats.test",
                "favorites": [],
            },
        )

    def _mock_pedidos(self, route) -> None:
        route.fulfill(
            status=200,
            json=[
                {
                    "id": 101,
                    "restaurant_id": 2,
                    "status": "confirmado",
                    "total_amount": 48.5,
                    "items": [
                        {"menu_id": 4, "quantity": 1, "price_at_time": 48.5},
                    ],
                }
            ],
        )
