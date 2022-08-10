import sys
import json
import thoth
import auxFunctions as aux

def insertTemplate (template):
    aux.checkDatabaseExist()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("templates", template["name"])
    texFilePathIntoElements = aux.copyFileIntoDatabase (template["name"], template["texFilePath"], "templates")
    aux.Database.executeCommand(f"""INSERT INTO templates (name, description, texFile)
    VALUES ('{template["name"]}','{template["description"]}','{texFilePathIntoElements}');""")
    thoth.addEntry (thoth.INFO, f"Template added with name {template['name']}")
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
    insertTemplate (element)

