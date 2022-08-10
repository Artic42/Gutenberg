import sys
import auxFunctions as aux
import thoth
import json

def insertColorPallete(name, red, blue, green, opacity):
    aux.checkDatabaseExist ()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("colors", name)
    aux.Database.executeCommand (f"""INSERT INTO colors
        (name, red, blue, green, opacity) VALUES
        ('{name}','{red}','{blue}','{green}','{opacity}');""")
    thoth.addEntry (thoth.INFO, f"Color added with name {name} to table colors")
    aux.closeDatabaseConnection()


def readColorJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as color file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["color"]

if __name__ == "__main__":
    log1 = thoth.log("insertColor", "/logs", thoth.INFO | thoth.ERROR, 30)
    element = readColorJSON (sys.argv[1])
    insertColorPallete (element["name"], element["red"], element["blue"], element["green"], element["opacity"])
    log1.closeLog()
