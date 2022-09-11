import os
import time
import thoth
import thothUtils
import fileManagement
import testEngine
import systemManagement as SM

def test ():
    if testEngine.env.isPassed():
        thoth.addEntry (thoth.INFO, "Execute the create database command with the database test json file")
        SM.command ("python3 src/databaseManager/createDatabase.py test/databaseManager/jsonFiles/database.json")
        thoth.addEntry (thoth.INFO, "Compare the created database with the empty reference database")
        SM.command ("sqldiff test/results/testDatabase.db test/databaseManager/emptyDatabase.db | tee test/results/diff")
        if fileManagement.checkFileEmpty("test/results/diff"):
            thoth.addEntry (thoth.INFO, "Both database are equal create database test PASSED")
            testEngine.env.passTest()
        else:
            thoth.addEntry (thoth.ERROR, "Both database are not equal, create database test is failed")
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()


if __name__ == "__main__":
    if fileManagement.checkExistsDir ("test/logs"):
        fileManagement.cleanDir("test/logs")
    log = thoth.log ("createDatabaseTest", "test/logs", thoth.INFO | thoth.ERROR, 30)
    testEngine.startTest ()
    test()
    time.sleep (1)
    testEngine.env.printResults ()
    testEngine.env.logResults ()
    thothUtils.mergeLog("test/logs", "mergedTestLog", "test/logs/mergedTestLog.log")