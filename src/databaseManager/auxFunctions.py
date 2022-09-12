import sqliteEngine
import thoth
import fileManagement
import sys
import date_time

def defineDatabasePath (path):
    global dbPath
    dbPath = path

def createDatabaseConnection ():
    global Database
    Database = sqliteEngine.sqliteConnection(dbPath)

def closeDatabaseConnection ():
    Database.commitClose()

def copyFileIntoDatabase (name, filePath, folder, extension):
    if filePath == "none" or fileManagement.checkExistsFile(filePath) == False:
        thoth.addEntry(thoth.INFO, "The file doesn't exist and won't be copied")
        return "none"
    elementsPath = Database.readEntryFiltered("value", "system", "parameter='elementsPath'")[0][0]
    texFileDestination = elementsPath + "/" + folder + "/" + str(name) + extension
    thoth.addEntry(thoth.INFO, f"File in {filePath} copied in {texFileDestination}")
    fileManagement.copyFile(filePath,texFileDestination)
    return texFileDestination

def deleteFileFromSystem (table, name):
    filePath = Database.readEntryFiltered ("texFile", table, f"name='{name}'")[0][0]
    fileManagement.deleteFile(filePath)

def databaseExist():
    return sqliteEngine.checkDatabaseExist(dbPath)

def checkDatabaseExist ():
    if sqliteEngine.checkDatabaseExist(dbPath)==False:
        thoth.addEntry(thoth.ERROR, "Database does not exist and ssytem can't continue")
        sys.exit(1)

def checkDatabaseNotPresent ():
    if sqliteEngine.checkDatabaseExist(dbPath)==True:
        thoth.addEntry(thoth.ERROR, "Database already exist and cannot be created again, system will exit")
        sys.exit(1)

def checkEntryExists (table, name):
    if Database.entryExistsOnTable (table, f"name='{name}'") == False:
        thoth.addEntry(thoth.ERROR, f"Entry with name {name} doesn't exist in {table}, cannot be deleted or added to preseet")
        sys.exit(2)

def checkNameEntryNotPresent (table, name):
    if Database.entryExistsOnTable (table, f"name='{name}'") == True:
        thoth.addEntry(thoth.ERROR, f"Entry with name {name} already exist in {table}, cannot be created")
        sys.exit(3)

def readSystemTable (parameter):
    value = Database.readEntryFiltered("value", "system", f"parameter='{parameter}'")[0][0]
    return value

def getFirstPendingJob ():
    value = Database.readEntry ("jobNumber", "pendingJobs")[0][0]
    return value

def move2Finshed (jobNumber):
    Database.executeCommand (f"""INSERT INTO finishedJobs
                                    SELECT * FROM pendingJobs
                                    WHERE jobNumber='{jobNumber}'""")
    Database.deleteEntryFromTable ("pendingJobs", f"jobNumber='{jobNumber}'")

def setFinishedDate (jobNumber):
    date = date_time.createDate()
    date.now()
    dateString = date.createString()
    Database.executeCommand (f"""UPDATE finishedJobs
                            SET dateFinished='{dateString}'
                            WHERE jobNumber='{jobNumber}'""")




