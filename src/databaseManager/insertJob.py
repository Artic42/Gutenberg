import sys
import json

import thoth
import auxFunctions as aux

def insertJob (job):
    aux.checkDatabaseExist()
    aux.createDatabaseConnection ()
    jobNumber = calculateJobNumber ()
    texFilePathIntoElements = aux.copyFileIntoDatabase (jobNumber, job["texFile"], "jobs", ".tex")
    elementsFilePathIntoElements = aux.copyFileIntoDatabase (jobNumber, job["elementsFiles"], "jobs", ".tar")
    aux.Database.executeCommand(f"""INSERT INTO pendingJobs (
                jobNumber,
                author,
                jiraStructure,
                title,
                epic,
                issue,
                template,
                colorPallete,
                generator,
                texFile,
                elementsFile,
                dateFinished)
    VALUES (
                '{jobNumber}',
                '{job["author"]}',
                '{job["jiraStructure"]}',
                '{job["title"]}',
                '{job["epic"]}',
                '{job["issue"]}',
                '{job["template"]}',
                '{job["colorPallete"]}',
                '{job["generator"]}',
                '{texFilePathIntoElements}',
                '{elementsFilePathIntoElements}',
                NULL);""")
    thoth.addEntry (thoth.INFO, f"Job added with number {jobNumber} and ")
    aux.closeDatabaseConnection()

def readJobJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as job file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["job"]

def calculateJobNumber ():
    pendingJobs = aux.Database.readEntry ("jobNumber", "pendingJobs")
    if pendingJobs != []:
        pendingJobs = list(pendingJobs [0])
    finishedJobs = aux.Database.readEntry ("jobNumber", "finishedJobs")
    if finishedJobs != []:
        finishedJobs = list(finishedJobs [0])
    jobs = pendingJobs + finishedJobs
    if jobs == []:
        highestJobNumber = 1000
    else:
        highestJobNumber = max(jobs)
    return highestJobNumber + 1

if __name__ == "__main__":
    thoth.log("insertJob", "/home/artic/Gutenberg/test/logs", thoth.INFO | thoth.ERROR, 30)
    element = readJobJSON (sys.argv[1])
    insertJob (element)