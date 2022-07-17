# This is a python project to get Share Data from NSE and update in the SQL Server

from Classes import ReadConfigFile
from Classes import ShareClass
from nsetools import Nse
import pandas as pd
import pyodbc


def quote_extractor(strStockCode):
    objNse = Nse()
    return objNse.get_quote(strStockCode)


#     Check and See if the result can be mapped to the Class Share. If so, return and use that.

if __name__ == '__main__':
    strConnString = ReadConfigFile.GetConnectionString()
    objConn = pyodbc.connect(strConnString)
    cursor = objConn.cursor()
    sqlResult = cursor.execute("SELECT* FROM [Shares].[dbo].[Shares]")
    for item in sqlResult:
        try:
            strRes = quote_extractor(item.Symbol)['closePrice']
            print(f"{item.Name}: {strRes}")
        except:
            print(f"{item.Name} not found in NSE Data")

    # strCode = input("Please enter the NSE Stock Code\n")
    # print(f"Previous Close Price of {strCode} is {quote_extractor(strCode)['closePrice']}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
