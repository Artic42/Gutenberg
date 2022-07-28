import sqliteEngine
import sys
import fileManagement

def deleteTemplate (dbPath, name):
    if sqliteEngine.checkDatabaseExist(dbPath)==False:
        return -1

    global Database
    Database = sqliteEngine.sqliteConnection(dbPath)

    if Database.entryExistsOnTable ("templates", f"name='{name}") == False:
        return -2

    deleteTexFileFromSystem (name)

    Database.deleteEntryFromTable("templates", f"name='{name}'")

    Database.commitClose()

    return 0

def deleteTexFileFromSystem (name):
    texFilePath = Database.readEntryFiltered ("texFile", "templates", f"name='{name}'")[0][0]
    fileManagement.deleteFile(texFilePath)

if __name__ == "__main__":
    exitCode = deleteTemplate (sys.argv[1], sys.argv[2])
    sys.exit(exitCode)