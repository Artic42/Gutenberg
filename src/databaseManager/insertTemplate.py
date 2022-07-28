import sys
import sqliteEngine
import fileManagement

def insertTemplate (dbPath, name, description, texFilePath):

    global Database
    Database = sqliteEngine.sqliteConnection(dbPath)

    texFilePathIntoElements = copyTexFileIntoDatabase (name, texFilePath)

    Database.executeCommand(f"""INSERT INTO templates (name, description, texFile)
    VALUES ('{name}','{description}','{texFilePathIntoElements}');""")

    Database.commitClose()
    del Database

def copyTexFileIntoDatabase (name, texFilePath):
    elementsPath = Database.readEntryFiltered("value", "system", "parameter='elementsPath'")[0][0]
    texFileDestination = elementsPath + "/templates/" + name + ".tex"
    fileManagement.copyFile(texFilePath,texFileDestination)
    return texFileDestination

if __name__ == "__main__":
    insertTemplate (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
