import sys
import auxFunctions as aux
import thoth
import json

def insertGenerator(generator):
    aux.checkDatabaseExist ()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("generators", generator["name"])
    shellScriptPath = aux.copyFileIntoDatabase (generator["name"], generator["shellScript"], "generators")
    aux.Database.executeCommand (f"""INSERT INTO colorPalletes
        (name,description, generatorCommand, shellScript) VALUES
        ('{generator["name"]}','{generator["description"]}','{generator["generatorCommand"]}','{shellScriptPath}');""")
    thoth.addEntry (thoth.INFO, f"Generator added with name {generator['name']}")
    aux.closeDatabaseConnection()

def readGeneratorJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as color pallete file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["generator"]

if __name__ == "__main__":
    log1 = thoth.log("insertColorPallete", "/logs", thoth.INFO | thoth.ERROR, 30)
    element = readGeneratorJSON (sys.argv[1])
    insertGenerator (element)
    log1.closeLog()