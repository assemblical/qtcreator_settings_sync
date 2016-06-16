from lib.Contants import Constants
from lib.Exporter import Exporter
from lib.Parser import Parser

if __name__ == '__main__':
    Constants.init()
    Parser.parseConfigJSON()
    Exporter.exportInitFile()
