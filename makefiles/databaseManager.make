databaseManager: createDatabase insertions deletion

createDatabase: bin/databaseManager/createDatabase.app
insertions: bin/databaseManager/insertColor.app bin/databaseManager/insertColorPallete.app bin/databaseManager/insertGenerator.app bin/databaseManager/insertJob.app bin/databaseManager/insertPreset.app bin/databaseManager/insertTemplate.app
deletion: bin/databaseManager/deleteEntry.app

bin/databaseManager/createDatabase.app: pythonInterpreter src/databaseManager/createDatabase.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/createDatabase.py > bin/databaseManager/createDatabase.app
	@echo createDatabase done

bin/databaseManager/insertColor.app: pythonInterpreter src/databaseManager/insertColor.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/insertColor.py > bin/databaseManager/insertColor.app
	@echo insertColor done

bin/databaseManager/insertColorPallete.app: pythonInterpreter src/databaseManager/insertColorPallete.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/insertColorPallete.py > bin/databaseManager/insertColorPallete.app
	@echo insertColorPallete done

bin/databaseManager/insertGenerator.app: pythonInterpreter src/databaseManager/insertGenerator.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/insertGenerator.py > bin/databaseManager/insertGenerator.app
	@echo insertGenerator done

bin/databaseManager/insertJob.app: pythonInterpreter src/databaseManager/insertJob.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/insertJob.py > bin/databaseManager/insertJob.app
	@echo insertJob done

bin/databaseManager/insertPreset.app: pythonInterpreter src/databaseManager/insertPreset.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/insertPreset.py > bin/databaseManager/insertPreset.app
	@echo insertPreset done

bin/databaseManager/insertTemplate.app: pythonInterpreter src/databaseManager/insertTemplate.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/insertTemplate.py > bin/databaseManager/insertTemplate.app
	@echo insertTemplate done

bin/databaseManager/deleteEntry.app: pythonInterpreter src/databaseManager/deleteEntry.py
	@mkdir -p bin
	@cat pythonInterpreter src/databaseManager/deleteEntry.py > bin/databaseManager/deleteEntry.app
	@echo deleteEntry done
