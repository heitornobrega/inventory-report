import re

# from simple_report import SimpleReport


class ColoredReport:
    def __init__(self, report_type):
        self.report_type = report_type

    def generate(self, products_list):
        report = self.report_type.generate(products_list)
        index_start = report.find("mais produtos:") + 15
        index_finish = report.find("\n", index_start)
        if index_finish == -1:
            index_finish = len(report)

        report = (
            report[:index_start]
            + "\033[31m"
            + report[index_start:index_finish]
            + "\033[0m"
            + report[index_finish:]
        )

        green_phrases = [
            "Data de fabricação mais antiga:",
            "Data de validade mais próxima:",
            "Empresa com mais produtos:",
        ]

        for phrase in green_phrases:
            report = report.replace(
                phrase,
                f"\033[32m{phrase}\033[0m",
            )

        report_dates = re.findall(r"(\d+-\d+-\d+)", report)

        for date in report_dates:
            report = report.replace(
                date,
                f"\033[36m{date}\033[0m",
            )

        return report


# relatorio = ColoredReport(SimpleReport).generate(
#     [
#         {
#             "id": 1,
#             "nome_do_produto": "Cafe",
#             "nome_da_empresa": "Cafes Nature",
#             "data_de_fabricacao": "2020-07-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "instrucao",
#         },
#         {
#             "id": 2,
#             "nome_do_produto": "Leite",
#             "nome_da_empresa": "Leite Monsanto",
#             "data_de_fabricacao": "2020-07-05",
#             "data_de_validade": "2030-03-09",
#             "numero_de_serie": "FR49",
#             "instrucoes_de_armazenamento": "instrucao",
#         },
#     ]
# )
# print(relatorio)
