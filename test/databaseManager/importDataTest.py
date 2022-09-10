import systemManagement as SM
import time
import thoth
import thothUtils
import fileManagement
import testEngine

def test ():
    if testEngine.env.isPassed():
        fileManagement.copyFile("test/databaseManager/emptyDatabase.db", "test/results/testDatabase.db")
        result1 = SM.command ("python3 src/databaseManager/insertTemplate.py test/databaseManager/jsonFiles/template1.json")
        result2 = SM.command ("python3 src/databaseManager/insertTemplate.py test/databaseManager/jsonFiles/template2.json")
        result3 = SM.command ("python3 src/databaseManager/insertTemplate.py test/databaseManager/jsonFiles/template3.json")
        if result1.ExitCode == 0 and result2.ExitCode == 0 and result3.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()
    
    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertTemplate.py test/databaseManager/jsonFiles/template1.json")
        if result.ExitCode == 3:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/deleteEntry.py test/databaseManager/jsonFiles/deletion.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertTemplate.py test/databaseManager/jsonFiles/template1.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertColor.py test/databaseManager/jsonFiles/color.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertColorPallete.py test/databaseManager/jsonFiles/colorPallete.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()
    
    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertGenerator.py test/databaseManager/jsonFiles/generator.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertPreset.py test/databaseManager/jsonFiles/preset.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertJob.py test/databaseManager/jsonFiles/job.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

    if testEngine.env.isPassed():
        result = SM.command ("python3 src/databaseManager/insertJob.py test/databaseManager/jsonFiles/job.json")
        if result.ExitCode == 0:
            testEngine.env.passTest()
        else:
            testEngine.env.failTest()
    else:
        testEngine.env.skipTest()

if __name__ == "__main__":
    if fileManagement.checkExistsDir ("test/logs"):
        fileManagement.cleanDir("test/logs")
    log = thoth.log ("importTemplateTest", "test/logs", thoth.INFO | thoth.ERROR, 30)
    testEngine.startTest ()
    test()
    time.sleep (1)
    testEngine.env.printResults ()
    testEngine.env.logResults ()
    thothUtils.mergeLog("test/logs", "mergedTestLog", "test/logs/mergedTestLog.log")