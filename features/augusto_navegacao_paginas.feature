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
