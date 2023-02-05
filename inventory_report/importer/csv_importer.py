from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, src):
        if "csv" in src:
            with open(src, "r") as file:
                data = list(csv.DictReader(file))
                return data
        else:
            raise ValueError("Arquivo inválido")
