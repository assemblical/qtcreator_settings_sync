from lib.Contants import Constants
from lib.Exporter import Exporter

if __name__ == '__main__':
    Constants.init()
    Exporter.exportInitFile([Constants.INI_FILE_CATEGORIES["GENERAL"], Constants.INI_FILE_CATEGORIES["CORE"]])
