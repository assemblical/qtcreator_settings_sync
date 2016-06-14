from Writer import Writer
from Contants import Constants

class Exporter:
    @staticmethod
    def exportInitFile(categories):
        w = Writer(Constants.EXPORTER_CONFIG_FILE)
        w.writeInitFile(categories)
