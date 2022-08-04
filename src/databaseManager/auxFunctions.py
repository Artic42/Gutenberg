import sqliteEngine
import fileManagement
import sys

def checkNameExist (table, name):
    result= Database.entryExistsOnTable(table, f"name='{name}'")
    return result

def createDatabaseConnection (dbPath):
    global Database
    Database = sqliteEngine.sqliteConnection(dbPath)

def closeDatabaseConnection ():
    Database.commitClose()
    del Database

def copyTexFileIntoDatabase (name, texFilePath, table):
    elementsPath = Database.readEntryFiltered("value", "system", "parameter='elementsPath'")[0][0]
    texFileDestination = elementsPath + "/" + table + "/" + name + ".tex"
    fileManagement.copyFile(texFilePath,texFileDestination)
    return texFileDestination

def deleteTexFileFromSystem (name, table):
    texFilePath = Database.readEntryFiltered ("texFile", table, f"name='{name}'")[0][0]
    fileManagement.deleteFile(texFilePath)

def checkDatabaseExist (dbPath):
    if sqliteEngine.checkDatabaseExist(dbPath)==False:
        sys.exit(-1)

def checkEntryExists (table, name):
    if Database.entryExistsOnTable (table, f"name='{name}") == False:
        sys.exit(-2)

def checkEntryNotPresent (table, name):
    if Database.entryExistsOnTable (table, f"name='{name}") == True:
        sys.exit(-3)