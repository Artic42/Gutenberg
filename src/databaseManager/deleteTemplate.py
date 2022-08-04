import sys
import auxFunctions as aux

def deleteTemplate (dbPath, name):
    aux.checkDatabaseExist
    aux.createDatabaseConnection (dbPath)
    aux.checkEntryExists("templates", name)
    aux.deleteTexFileFromSystem (name)
    aux.Database.deleteEntryFromTable("templates", f"name='{name}'")
    aux.closeDatabaseConnection ()

if __name__ == "__main__":
    deleteTemplate (sys.argv[1], sys.argv[2])
