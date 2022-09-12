import auxFunctions as aux


def insertItem (parameter, value):
    aux.Database.executeCommand (f"""INSERT INTO system (parameter, value) 
                        VALUES ('{parameter}', '{value}');""")

def updateItem (parameter, value):
    aux.Database.executeCommand (f"""UPDATE system 
                                SET value={value}
                                WHEN parameter={parameter}""")

def setJobInProgress ():
    updateItem ("jobInProgress", "TRUE")

def resetJobInProgress ():
    updateItem ("jobInProgress", "FALSE")

def isJobInProgress ():
    aux.readSystemTable ("jobInProgress")