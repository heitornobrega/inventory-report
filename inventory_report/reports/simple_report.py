from datetime import datetime
from collections import Counter


class SimpleReport:
    _fabricacao_mais_antiga = None
    _validade_mais_proxima = None
    _empresa_com_maior_estoque = ""

    @classmethod
    def __get_min_date(cls, key: str, lista: list):
        def get_date(produto):
            return datetime.strptime(produto[key], "%Y-%m-%d")

        produto = min(lista, key=get_date)
        return produto[key]

    @classmethod
    def __get_most_common_company(cls, lista: list):
        empresas = []
        for produto in lista:
            empresas.append(produto["nome_da_empresa"])
        cls._empresa_com_maior_estoque = Counter(empresas).most_common(1)[0][0]
        return cls._empresa_com_maior_estoque

    @classmethod
    def generate(cls, lista: list):
        cls._fabricacao_mais_antiga = cls.__get_min_date(
            "data_de_fabricacao", lista
        )
        cls._validade_mais_proxima = cls.__get_min_date(
            "data_de_validade", lista
        )
        cls._empresa_com_maior_estoque = cls.__get_most_common_company(lista)

        return (
            f"Data de fabricação mais antiga: {cls._fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {cls._validade_mais_proxima}\n"
            f"Empresa com mais produtos: {cls._empresa_com_maior_estoque}"
        )
