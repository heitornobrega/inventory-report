from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator

# from inventory_report.importer.csv_importer import CsvImporter


class ITiposRelatorios:
    simples = "simples"
    completo = "completo"


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []
        self.stop = 0

    def import_data(self, src: str, tipo_relatorio: ITiposRelatorios):
        self.data += self.importer.import_data(src)
        self.stop += len(self.data)
        if tipo_relatorio == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.stop, self.data)
