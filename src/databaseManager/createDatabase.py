import sqlite3
import sys
import os
import fileManagement

def deleteDatabase(pathDB):
    os.remove(pathDB)

def createDatabase (pathDB, pathElements):
    if os.path.isfile (pathDB):
        return -1

    db = sqlite3.connect (pathDB)
    fileManagement.createDir (pathElements)
    
    createSystemTable (db, pathElements)
    createTemplatesTable (db)
    createColorPalletesTable (db)
    createPresetsTable (db)
    createGeneratorTable (db)
    createJobsTables (db)

    db.commit()
    db.close()

def createSystemTable (database, pathElements):
    dbCursor = database.cursor()

    dbCursor.execute("""CREATE TABLE system(
        parameter text,
        value text
        )""")

    dbCursor.execute(f"""INSERT INTO system (parameter, value) 
                        VALUES ('elementsPath', '{pathElements}');""")

def createTemplatesTable (database):
    dbCursor = database.cursor()
    dbCursor.execute ("""CREATE TABLE templates(
        name text,
        description text,
        texFile text)
    """)

def createColorPalletesTable (database):
    dbCursor = database.cursor()
    dbCursor.execute ("""CREATE TABLE colorPalletes(
        name text,
        description text,
        backgroundColor text,
        letterColor text,
        texFile text)
    """)

def createPresetsTable (database):
    dbCursor = database.cursor()
    dbCursor.execute ("""CREATE TABLE presets(
        name text,
        description text,
        template text,
        colorPallete text,
        generator text
        )""")

def createGeneratorTable (database):
    dbCursor = database.cursor()
    dbCursor.execute ("""CREATE TABLE generators(
        name text,
        description text,
        generatorCommand text)
    """)

def createJobsTables (database):
    dbCursor = database.cursor()
    dbCursor.execute ("""CREATE TABLE pendingJobs(
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

    dbCursor.execute ("""CREATE TABLE finishedJobs(
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