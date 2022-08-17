import os
import thoth
import mergeLogDir
import fileManagement
import testEngine

def test ():
    if testEngine.env.isPassed():
        thoth.addEntry (thoth.INFO, "Execute the create database command with the database test json file")
        os.system ("python3 src/databaseManager/createDatabase.py test/databaseManager/jsonFiles/database.json")
        thoth.addEntry (thoth.INFO, "Compare the created database with the empty reference database")
        os.system ("sqldiff test/results/testDatabase.db test/databaseManager/emptyDatabase.db | tee test/results/diff")
        if fileManagement.checkFileEmpty("test/results/diff"):
            thoth.addEntry (thoth.INFO, "Both database are equal create database test PASSED")
            testEngine.env.passTest()
        else:
            thoth.addEntry (thoth.ERROR, "Both database are not equal, create database test is failed")
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()


if __name__ == "__main__":
    fileManagement.cleanDir("test/logs")
    log = thoth.log ("createDatabaseTest", "test/logs", thoth.INFO | thoth.ERROR, 30)
    testEngine.startTest ()
    test()
    testEngine.env.printResults ()
    testEngine.env.logResults ()
    mergeLogDir.main("test/logs", "test/logs/log")