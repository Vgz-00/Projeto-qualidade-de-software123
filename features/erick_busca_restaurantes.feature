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
