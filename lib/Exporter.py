from lib.Writer import Writer
from lib.Contants import Constants

class Exporter:
    @staticmethod
    def exportInitFile():
        w = Writer(Constants.EXPORTER_CONFIG_FILE)
        w.writeInitFile(Constants.CONFIG_INI_FILE_CATEGORIES)
