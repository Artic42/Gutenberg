import sys
import json
import auxFunctions as aux
import thoth

def deleteEntry (table, name):
    aux.checkDatabaseExist()
    aux.createDatabaseConnection()
    aux.checkEntryExists(table, name)
    if table == "templates":
        aux.deleteTexFileFromSystem (table, name)
    aux.Database.deleteEntryFromTable(table, f"name='{name}'")
    thoth.addEntry (thoth.INFO, f"Entry deleted from {table} with name {name}")
    aux.closeDatabaseConnection ()

def readDeletionJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as deletion command file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["delete"]

if __name__ == "__main__":
    log1 = thoth.log ("deleteEntry", "/logs", thoth.INFO | thoth.ERROR, 30)
    entry = readDeletionJSON (sys.argv[1])
    deleteEntry (entry["table"], entry["name"])
