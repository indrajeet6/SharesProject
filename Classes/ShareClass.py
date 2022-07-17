class Share:
    Symbol = ""
    Name = ""
    MktValue = 0.00
    Count = 0
    Total = 0
    LastUpdateTime = ""

    def __init__(self, strSymbol="", strName="", fltMktValue=0.00, intCount=0, intTotal=0, strLastUpdateTime=""):
        self.Symbol = strSymbol
        self.Name = strName
        self.MktValue = fltMktValue
        self.Count = intCount
        self.Total = intTotal
        self.LastUpdateTime = strLastUpdateTime

    def total_value(self):
        return self.Count * self.MktValue
