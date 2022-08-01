import sqliteEngine

def checkNameExist (table, name):
    result= Database.entryExistsOnTable(table, f"name='{name}'")
    return result

def createDatabaseConnection (dbPath);
    global Database
    Database = sqliteEngine.sqliteConnection(dbPath)