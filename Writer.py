from Contants import Constants
from Parser import Parser
import os


class Writer:

    def __init__(self, fileName):
        if not os.path.exists(Constants.EXPORTER_DIR):
            os.makedirs(Constants.EXPORTER_DIR)
        self.f = open(fileName, 'w+')

    def writeInitFile(self, categories):
        p = Parser(Constants.QTCREATOR_CONFIG_FILE)
        for cat in categories:
            self.f.write(p.parseIniFileCategorie(cat) + '\n')
