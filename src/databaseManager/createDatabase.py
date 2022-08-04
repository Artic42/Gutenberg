import sys
import os
import fileManagement
import auxFunctions as aux

def deleteDatabase(pathDB):
    os.remove(pathDB)

def createDatabase (pathDB, pathElements):
    aux.checkDatabaseExist (pathDB)
    aux.createDatabaseConnection (pathDB)
    fileManagement.createDir (pathElements)
    
    createSystemTable (pathElements)
    createDirStructureInElements (pathElements)
    createTemplatesTable ()
    createColorPalletesTable ()
    createPresetsTable ()
    createGeneratorTable ()
    createJobsTables ()

    aux.Database.commitClose()

def createSystemTable (pathElements):
    aux.Database.executeCommand ("""CREATE TABLE system(
        parameter text,
        value text
        )""")

    aux.Database.executeCommand (f"""INSERT INTO system (parameter, value) 
                        VALUES ('elementsPath', '{pathElements}');""")
    

def createDirStructureInElements (pathElements):
    fileManagement.createDir(pathElements+"/templates")
    fileManagement.createDir(pathElements+"/colorPalletes")
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
        letterColor text,
        texFile text)
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

if __name__ == "__main__":
    if len(sys.argv)>=3 and os.path.isfile(sys.argv[1]):
        deleteDatabase(sys.argv[1])
    createDatabase(sys.argv[1], sys.argv[2])