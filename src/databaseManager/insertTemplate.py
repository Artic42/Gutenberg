import sys
import auxFunctions as aux

def insertTemplate (dbPath, name, description, texFilePath):
    aux.checkDatabaseExist(dbPath)
    aux.createDatabaseConnection (dbPath)
    aux.checkEntryNotPresent("Templates", name)
    texFilePathIntoElements = aux.copyTexFileIntoDatabase (name, texFilePath)
    aux.Database.executeCommand(f"""INSERT INTO templates (name, description, texFile)
    VALUES ('{name}','{description}','{texFilePathIntoElements}');""")
    aux.closeDatabaseConnection()


if __name__ == "__main__":
    insertTemplate (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

