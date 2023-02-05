import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Verifique os argumentos")
        sys.exit(1)

    path = sys.argv[1]
    type = sys.argv[2]
    print(len(sys.argv))
    formato = path.split("/")[-1].split(".")[-1]
    objeto = None
    if formato == "csv":
        objeto = InventoryRefactor(CsvImporter)
    elif formato == "json":
        objeto = InventoryRefactor(JsonImporter)
    elif formato == "xml":
        objeto = InventoryRefactor(XmlImporter)

    report = objeto.import_data(path, type)

    sys.stderr.write(report)
    sys.exit(1)


if __name__ == "__main__":
    main()
