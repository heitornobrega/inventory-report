from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, src):
        if "json" in src:
            with open(src, "r") as file:
                data = list(json.load(file))
                return data
        else:
            raise ValueError("Arquivo inválido")
