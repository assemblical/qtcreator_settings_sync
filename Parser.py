from Contants import Constants


class Parser:

    def __init__(self, fileName):
        self.f = open(fileName, 'r')
        self.parseIniFile()

    def parseIniFile(self):
        for k, v in Constants.INI_FILE_CATEGORIES.items():
            return self.parseIniFileCategorie(v)

    def parseIniFileCategorie(self, categorieName):
        self.f.seek(0) # reset stream to the beginning
        return self.parseRange(categorieName, '\n')

    def parseRange(self, startStr, endStr):
        resultStr = ""
        for line in self.f:
            if line.startswith(startStr):
                rangeF = self.f
                resultStr = line
                for rangeLine in rangeF:
                    if rangeLine.startswith(endStr):
                        return resultStr
                    resultStr += rangeLine

