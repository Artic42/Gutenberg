import sys
import sqliteEngine
import fileManagement

def insertTemplate (dbPath, name, description, texFilePath):
    if sqliteEngine.checkDatabaseExist(dbPath)==False:
        return -1
    
    global Database
    Database = sqliteEngine.sqliteConnection(dbPath)

    #LOG Error template name already exist on system
    if checkNameExist(name) == True:
        return -2

    texFilePathIntoElements = copyTexFileIntoDatabase (name, texFilePath)

    Database.executeCommand(f"""INSERT INTO templates (name, description, texFile)
    VALUES ('{name}','{description}','{texFilePathIntoElements}');""")

    Database.commitClose()
    del Database
    return 0

def copyTexFileIntoDatabase (name, texFilePath):
    elementsPath = Database.readEntryFiltered("value", "system", "parameter='elementsPath'")[0][0]
    texFileDestination = elementsPath + "/templates/" + name + ".tex"
    fileManagement.copyFile(texFilePath,texFileDestination)
    return texFileDestination

def checkNameExist (name):
    result= Database.entryExistsOnTable("templates", f"name='{name}'")
    return result

if __name__ == "__main__":
    exitCode = insertTemplate (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    sys.exit(exitCode)
