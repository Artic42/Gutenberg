import sqliteEngine
import sys
import fileManagement

def insertColorPallete(dbPath, name, description, texFile, backgroundColor, letterColor):
    if sqliteEngine.checkDatabaseExist(dbPath)==False:
        return -1

    

    #LOG Error template name already exist on system
    if checkNameExist(name) == True:
        return -2