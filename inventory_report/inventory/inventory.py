from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class ITiposRelatorios:
    simples = "simples"
    completo = "completo"


class Inventory:
    @classmethod
    def import_data(cls, src: str, tipo_relatorio: ITiposRelatorios):
        data = []
        if "csv" in src:
            data = CsvImporter().import_data(src)
        if "json" in src:
            data = JsonImporter().import_data(src)
        if "xml" in src:
            data = XmlImporter().import_data(src)
        if tipo_relatorio == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
