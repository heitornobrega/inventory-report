from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    companies = []

    @classmethod
    def company_counter(cls, lista: list):
        empresas = []
        for produto in lista:
            empresas.append(produto["nome_da_empresa"])
        cls.companies = dict(Counter(empresas))
        return cls.companies

    @staticmethod
    def formater(dicionario: dict):
        string = ""
        for key, value in dicionario.items():
            string += f"- {key}: {value}\n"
        return string

    @classmethod
    def generate(cls, lista: list):
        # print(super().generate(lista))
        cls.company_counter(lista)
        return (
            f"{super().generate(lista)}\n"
            f"Produtos estocados por empresa:\n"
            f"{cls.formater(cls.companies)}"
        )
