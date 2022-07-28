import sqliteConnection
import sys
import os
import fileManagement

def deleteDatabase(pathDB):
    os.remove(pathDB)

def createDatabase (pathDB, pathElements):
    if sqliteConnection.checkDatabaseExist(pathDB) == False:
        return -1

    global Database
    Database = sqliteConnection.sqliteConnection (pathDB)
    fileManagement.createDir (pathElements)
    
    createSystemTable (pathElements)
    createTemplatesTable ()
    createColorPalletesTable ()
    createPresetsTable ()
    createGeneratorTable ()
    createJobsTables ()

    Database.commitClose()

def createSystemTable (pathElements):
    Database.executeCommand ("""CREATE TABLE system(
        parameter text,
        value text
        )""")

    Database.executeCommand (f"""INSERT INTO system (parameter, value) 
                        VALUES ('elementsPath', '{pathElements}');""")

def createTemplatesTable ():
    
    Database.executeCommand  ("""CREATE TABLE templates(
        name text,
        description text,
        texFile text)
    """)

def createColorPalletesTable ():
    
    Database.executeCommand  ("""CREATE TABLE colorPalletes(
        name text,
        description text,
        backgroundColor text,
        letterColor text,
        texFile text)
    """)

def createPresetsTable ():
    
    Database.executeCommand  ("""CREATE TABLE presets(
        name text,
        description text,
        template text,
        colorPallete text,
        generator text
        )""")

def createGeneratorTable ():
    
    Database.executeCommand  ("""CREATE TABLE generators(
        name text,
        description text,
        generatorCommand text)
    """)

def createJobsTables ():
    
    Database.executeCommand  ("""CREATE TABLE pendingJobs(
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

    Database.executeCommand  ("""CREATE TABLE finishedJobs(
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