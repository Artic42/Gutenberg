import sys
import auxFunctions as aux
import thoth
import json

def insertPreset(preset):
    aux.checkDatabaseExist ()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("Presets", preset["name"])
    aux.checkEntryExists("templates", preset["template"])
    aux.checkEntryExists("colorPalletes", preset["colorPallete"])
    aux.checkEntryExists("generators", preset["generator"])
    aux.Database.executeCommand (f"""INSERT INTO presets
        (name, description, template, colorPallete, generator) VALUES
        ('{preset["name"]}',
        '{preset["description"]}',
        '{preset["template"]}',
        '{preset["colorPallete"]}',
        '{preset["generator"]}');""")
    thoth.addEntry (thoth.INFO, f"Preset added with name {preset['name']}")
    aux.closeDatabaseConnection()

def readPresetJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as color pallete file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["preset"]

if __name__ == "__main__":
    log1 = thoth.log("insertPreset", "/home/artic/Gutenberg/test/logs", thoth.INFO | thoth.ERROR, 30)
    element = readPresetJSON (sys.argv[1])
    insertPreset (element)
    log1.closeLog()