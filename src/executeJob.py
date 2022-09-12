import thoth
import sys
from databaseManager import auxFunctions as aux
import json

def execute (job):
    pass

def readJob (jobNumber):
    pass

def readJobJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as job file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])

if __name__ == "__main__":
    readJobJSON (sys.argv[1])
    aux.createDatabaseConnection()
    number = aux.getFirstPendingJob()
    job = readJob (number)
    execute (job)
    aux.move2Finshed (number)
    aux.setFinishedDate (number)

    aux.Database.commitClose()
