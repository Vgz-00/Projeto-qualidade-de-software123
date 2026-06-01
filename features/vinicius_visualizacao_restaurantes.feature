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
