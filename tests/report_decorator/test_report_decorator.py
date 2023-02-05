from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

# from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    produtos = [
        {
            "id": 1,
            "nome_do_produto": "Cafe",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao",
        },
        {
            "id": 2,
            "nome_do_produto": "Leite",
            "nome_da_empresa": "Leite Monsanto",
            "data_de_fabricacao": "2020-07-05",
            "data_de_validade": "2030-03-09",
            "numero_de_serie": "FR49",
            "instrucoes_de_armazenamento": "instrucao",
        },
    ]
    relatorio_simples = ColoredReport(SimpleReport).generate(produtos)
    # relatorio_completo = ColoredReport(CompleteReport).generate(produtos)
    assert (
        relatorio_simples
        == "\033[32mData de fabricação "
        + "mais antiga:\033[0m \033[36m2020-07-04\033[0m\n"
        + "\033[32mData de validade "
        + "mais próxima:\033[0m \033[36m2023-02-09\033[0m\n"
        + "\033[32mEmpresa com mais "
        + "produtos:\033[0m \033[31mCafes Nature\033[0m"
    )


# assert relatorio_completo == CompleteReport.generate(produtos)
