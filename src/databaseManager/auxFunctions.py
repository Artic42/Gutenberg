from asyncio.constants import DEBUG_STACK_DEPTH
import sqliteEngine
import thoth
import fileManagement
import sys



def defineDatabasePath (path):
    global dbPath
    dbPath = path

def createDatabaseConnection ():
    global Database
    Database = sqliteEngine.sqliteConnection(dbPath)

def closeDatabaseConnection ():
    Database.commitClose()

def copyTexFileIntoDatabase (name, texFilePath, table):
    elementsPath = Database.readEntryFiltered("value", "system", "parameter='elementsPath'")[0][0]
    texFileDestination = elementsPath + "/" + table + "/" + name + ".tex"
    fileManagement.copyFile(texFilePath,texFileDestination)
    return texFileDestination

def deleteTexFileFromSystem (table, name):
    texFilePath = Database.readEntryFiltered ("texFile", table, f"name='{name}'")[0][0]
    fileManagement.deleteFile(texFilePath)

def databaseExist():
    return sqliteEngine.checkDatabaseExist(dbPath)

def checkDatabaseExist ():
    if sqliteEngine.checkDatabaseExist(dbPath)==False:
        thoth.addEntry(thoth.ERROR, "Database does not exist and ssytem can't continue")
        sys.exit(-1)

def checkDatabaseNotPresent ():
    if sqliteEngine.checkDatabaseExist(dbPath)==True:
        thoth.addEntry(thoth.ERROR, "Database already exist and cannot be created again, system will exit")
        sys.exit(-1)

def checkEntryExists (table, name):
    if Database.entryExistsOnTable (table, f"name='{name}'") == False:
        thoth.addEntry(thoth.ERROR, f"Entry with name {name} doesn't exist in {table}, cannot be deleted")
        sys.exit(-2)

def checkEntryNotPresent (table, name):
    if Database.entryExistsOnTable (table, f"name='{name}'") == True:
        thoth.addEntry(thoth.ERROR, f"Entry with name {name} already exist in {table}, cannot be created")
        sys.exit(-3)


