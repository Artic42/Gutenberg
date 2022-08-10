import sys
import auxFunctions as aux
import thoth
import json

def insertColorPallete(colorPallete):
    aux.checkDatabaseExist ()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("colorPalletes", colorPallete["name"])
    aux.Database.executeCommand (f"""INSERT INTO colorPalletes
        (name,description,backgroundColor, letterColor) VALUES
        ('{colorPallete["name"]}',
        '{colorPallete["description"]}',
        '{colorPallete["backgroundColor"]}',
        '{colorPallete["letterColor"]}');""")
    thoth.addEntry (thoth.INFO, f"Color pallete added with name {colorPallete['name']}")
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
    insertColorPallete (element)
    log1.closeLog()

