import sys
import auxFunctions as aux
import thoth
import json

def insertColorPallete(name, description, backgroundColor, letterColor):
    aux.checkDatabaseExist ()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("colorPalletes", name)
    aux.Database.executeCommand (f"""INSERT INTO colorPalletes
        (name,description,backgroundColor, letterColor) VALUES
        ('{name}','{description}','{backgroundColor}','{letterColor}');""")
    thoth.addEntry (thoth.INFO, f"Color pallete added with name {name}")
    aux.closeDatabaseConnection()


def readColorPalleteJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as color pallete file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["colorPallete"]

if __name__ == "__main__":
    log1 = thoth.log("insertColorPallete", "/logs", thoth.INFO | thoth.ERROR, 30)
    element = readColorPalleteJSON (sys.argv[1])
    insertColorPallete (element["name"], element["description"], element["backgroundColor"], element["letterColor"])
    log1.closeLog()

