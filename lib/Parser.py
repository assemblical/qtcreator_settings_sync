from lib.Contants import Constants
import json


class Parser:

    def __init__(self, fileName):
        self.f = open(fileName, 'r')
        self.parseIniFile()

    def parseIniFile(self):
        Parser.parseConfigJSON()
        for v in Constants.CONFIG_INI_FILE_CATEGORIES:
            return self.parseIniFileCategorie(v)

    def parseIniFileCategorie(self, categorieName):
        self.f.seek(0) # reset stream to the beginning
        return self.parseRange(categorieName, '\n')

    # parse file range from startStr to endStr
    def parseRange(self, startStr, endStr):
        for line in self.f:
            if line.startswith("[" + startStr):
                rangeF = self.f
                resultStr = line
                for rangeLine in rangeF:
                    if rangeLine.startswith(endStr):
                        return resultStr
                    resultStr += rangeLine

    @staticmethod
    def parseConfigJSON():
        with open(Constants.SYNC_CONFIG_FILE) as configJSON:
           jsonData = json.load(configJSON)
           Constants.CONFIG_INI_FILE_CATEGORIES = jsonData["INI_FILE_CATEGORIES"]
