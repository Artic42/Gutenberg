import sys
import json
import thoth
import auxFunctions as aux

def insertTemplate (name, description, texFilePath):
    aux.checkDatabaseExist()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("templates", name)
    texFilePathIntoElements = aux.copyTexFileIntoDatabase (name, texFilePath, "templates")
    aux.Database.executeCommand(f"""INSERT INTO templates (name, description, texFile)
    VALUES ('{name}','{description}','{texFilePathIntoElements}');""")
    thoth.addEntry (thoth.INFO, f"Template added with name {name}")
    aux.closeDatabaseConnection()

def readTemplateJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as template file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["template"]

if __name__ == "__main__":
    thoth.log("insertTemplate", "/logs", thoth.INFO | thoth.ERROR, 30)
    element = readTemplateJSON (sys.argv[1])
    insertTemplate (element["name"], element["description"], element["texFile"])

