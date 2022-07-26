import sqlite3
import sys
import os

def deleteDatabase(pathDB):
    os.remove(pathDB)

def createDatabase (pathDB, pathElements):
    if os.path.isfile (pathDB):
        return -1

    db = sqlite3.connect (pathDB)
    if os.path.isdir(pathElements)==False:
        os.mkdir (pathElements)
    dbCursor = db.cursor()

    dbCursor.execute ("""CREATE TABLE system(
        parameter text,
        value text
        )""")

    dbCursor.execute (f"""INSERT INTO system (parameter, value) 
                        VALUES ('elementsPath', '{pathElements}');""")

    dbCursor.execute ("""CREATE TABLE templates(
        name text,
        description text,
        texFile text)
    """)

    dbCursor.execute ("""CREATE TABLE colorPalletes(
        name text,
        description text,
        backgroundColor text,
        letterColor text,
        texFile text)
    """)

    dbCursor.execute ("""CREATE TABLE generators(
        name text,
        description text,
        generatorCommand text)
    """)

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

    db.commit()
    db.close()


if __name__ == "__main__":
    if len(sys.argv)>=3 and os.path.isfile(sys.argv[1]):
        deleteDatabase(sys.argv[1])
    createDatabase(sys.argv[1], sys.argv[2])