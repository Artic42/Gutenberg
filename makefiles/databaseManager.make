databaseManager: createDatabase

createDatabase: bin/createDatabase

bin/createDatabase: pythonInterpreter src/databaseManager/createDatabase.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/createDatabase.py > bin/createDatabase
	@echo createDatabase done