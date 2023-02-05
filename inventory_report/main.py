import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Verifique os argumentos\n")

    caminho = sys.argv[1]
    tipo_relatorio = sys.argv[-1]
    formato = caminho.split("/")[-1].split(".")[-1]

    if formato == "csv":
        objeto = InventoryRefactor(CsvImporter)
        report = objeto.import_data(caminho, tipo_relatorio)
        sys.stdout.write(report)

    elif formato == "json":
        objeto = InventoryRefactor(JsonImporter)
        report = objeto.import_data(caminho, tipo_relatorio)
        sys.stdout.write(report)

    elif formato == "xml":
        objeto = InventoryRefactor(XmlImporter)
        report = objeto.import_data(caminho, tipo_relatorio)
        sys.stdout.write(report)
