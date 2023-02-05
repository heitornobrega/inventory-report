from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, src):
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
