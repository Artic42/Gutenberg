import sys
import json
import os
import fileManagement
import thoth
import auxFunctions as aux

def deleteDatabase():
    os.remove(aux.dbPath)
    thoth.addEntry(thoth.INFO, f"Database deleted in path {aux.dbPath}")

def createDatabase (pathElements):
    aux.checkDatabaseNotPresent ()
    aux.createDatabaseConnection ()
    fileManagement.createDir (pathElements)
    
    createSystemTable (pathElements)
    createDirStructureInElements (pathElements)
    createTemplatesTable ()
    createColorPalletesTable ()
    createPresetsTable ()
    createGeneratorTable ()
    createJobsTables ()
    thoth.addEntry(thoth.INFO, f"Database creted with default information in path {aux.dbPath}")

    aux.Database.commitClose()

def createSystemTable (pathElements):
    aux.Database.executeCommand ("""CREATE TABLE system(
        parameter text,
        value text
        )""")

    aux.Database.executeCommand (f"""INSERT INTO system (parameter, value) 
                        VALUES ('elementsPath', '{pathElements}');""")
    

def createDirStructureInElements (pathElements):
    fileManagement.createDir(pathElements)
    fileManagement.createDir(pathElements+"/templates")
    fileManagement.createDir(pathElements+"/jobs")

def createTemplatesTable ():
    
    aux.Database.executeCommand  ("""CREATE TABLE templates(
        name text,
        description text,
        texFile text)
    """)

def createColorPalletesTable ():
    
    aux.Database.executeCommand  ("""CREATE TABLE colorPalletes(
        name text,
        description text,
        backgroundColor text,
        letterColor text)
    """)

    aux.Database.executeCommand ("""CREATE TABLE colors (
        name text,
        red int,
        green int,
        blue int,
        opacity int)
    """)

def createPresetsTable ():
    
    aux.Database.executeCommand  ("""CREATE TABLE presets(
        name text,
        description text,
        template text,
        colorPallete text,
        generator text
        )""")

def createGeneratorTable ():
    
    aux.Database.executeCommand  ("""CREATE TABLE generators(
        name text,
        description text,
        generatorCommand text)
    """)

def createJobsTables ():
    
    aux.Database.executeCommand  ("""CREATE TABLE pendingJobs(
        jobNumber int,
        author text,
        jiraStructure int, 
        title text,
        epic text,
        issue text,
        template text,
        colorPallete text,
        generator text,
        texFile text,
        elementsFile text)
    """)

    aux.Database.executeCommand  ("""CREATE TABLE finishedJobs(
        jobNumber int,
        author text,
        jiraStructure int, 
        title text,
        epic text,
        issue text,
        template text,
        colorPallete text,
        generator text,
        texFile text,
        elementsFile text)
    """)

def readDatabaseJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as database file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data

if __name__ == "__main__":
    log1 = thoth.log("createDatabase", "/logs", thoth.INFO | thoth.ERROR, 20)
    data = readDatabaseJSON (sys.argv[1])
    if data["replace"]=="True" and aux.databaseExist():
        thoth.addEntry(thoth.INFO, "System detected database already exist and there is order to replace")
        deleteDatabase()
    createDatabase(data["elementsPath"])
    log1.closeLog()