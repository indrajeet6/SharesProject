import os
import json


def GetConnectionString():
    strConnString = ""
    strConfigFile = os.path.join(os.path.relpath("Config"), "appsettings.json")
    if os.path.isfile(strConfigFile):
        with open(strConfigFile, "r") as jsonfile:
            strConnString = json.load(jsonfile)["ConnectionStrings"]["MSIDB"]
            return strConnString
