include makefiles/databaseManager.make



all: databaseManager execution

clean: 
	@rm -f bin/*.app
	@rm -f bin/databaseManager/*.app
	@rm -rf test/logs
	@rm -rf test/results
	@echo Repo cleaned

install:

execution: bin/executeJob.app
	@mkdir -p bin
	@cat pythonInterpreter src/executeJob.py > bin/executeJob.app
	@echo executeJob done

bin/executeJob.app: src/executeJob.py pythonInterpreter