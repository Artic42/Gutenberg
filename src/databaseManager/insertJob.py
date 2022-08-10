import sys
import json
import thoth
import auxFunctions as aux

def insertJob (job):
    aux.checkDatabaseExist()
    aux.createDatabaseConnection ()
    aux.checkEntryNotPresent("pendingJobs", job["jobNumber"])
    texFilePathIntoElements = aux.copyFileIntoDatabase (job["jobNumber"], job["texFile"], "pendingJobs", ".tex")
    elementsFilePathIntoElements = aux.copyFileIntoDatabase (job["jobNumber"], job["elementsFile"], "pendingJobs", ".tar")
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
                autoPublish,
                texFile,
                elementsFile)
    VALUES (
                '{job["jobNumber"]}',
                '{job["author"]}',
                '{job["jiraStructure"]},
                '{job["title"]},
                '{job["epic"]}',
                '{job["issue"]}',
                '{job["template"]}',
                '{job["colorPallete"]},
                '{job["generator"]}',
                '{job["autoPublish"]}',
                '{texFilePathIntoElements}',
                '{elementsFilePathIntoElements}');""")
    thoth.addEntry (thoth.INFO, f"Job added with number {job['jobNumber']} and ")
    aux.closeDatabaseConnection()

def readJobJSON (jsonPath):
    thoth.addEntry(thoth.INFO, f"Json file {jsonPath} read, and loaded as job file")
    file = open(jsonPath)
    data = json.load(file)
    aux.defineDatabasePath(data["dbPath"])
    return data ["job"]

if __name__ == "__main__":
    thoth.log("insertJob", "/logs", thoth.INFO | thoth.ERROR, 30)
    element = readJobJSON (sys.argv[1])
    insertJob (element["name"], element["description"], element["texFile"])