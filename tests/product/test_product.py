from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        id=1,
        nome_da_empresa="Padaria",
        nome_do_produto="Pão",
        data_de_fabricacao="10/01/2023",
        data_de_validade="10/01/2024",
        numero_de_serie="45adfd56axx00",
        instrucoes_de_armazenamento="em local úmido e abafado.",
    )
    assert produto.__repr__() == (
        f"O produto {produto.nome_do_produto}"
        f" fabricado em {produto.data_de_fabricacao}"
        f" por {produto.nome_da_empresa} com validade"
        f" até {produto.data_de_validade}"
        f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
    )
