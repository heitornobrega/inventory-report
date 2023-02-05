import csv
import json
import xml.etree.ElementTree as ET


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class ITiposRelatorios:
    simples = "simples"
    completo = "completo"


class Inventory:
    @classmethod
    def csv_reader(cls, src: str):
        with open(src, "r") as file:
            data = list(csv.DictReader(file))
            return data

    @classmethod
    def json_reader(cls, src: str):
        with open(src, "r") as file:
            data = list(json.load(file))
            return data

    @classmethod
    def xml_reader(cls, src: str):
        list_test = []
        with open(src, "r") as file:
            tree = ET.parse(file)
            root = tree.getroot()
        for element in root:
            dict = {}
            for child in element:
                dict[child.tag] = child.text
            list_test.append(dict)
        return list_test

    @classmethod
    def import_data(cls, src: str, tipo_relatorio: ITiposRelatorios):
        data = []
        if "csv" in src:
            data = cls.csv_reader(src)
        if "json" in src:
            data = cls.json_reader(src)
        if "xml" in src:
            data = cls.xml_reader(src)
        if tipo_relatorio == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
