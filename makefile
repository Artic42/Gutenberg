include makefiles/databaseManager.make
include makefiles/execute.make


all: databaseManager execution

clean: 
	@rm -f bin/*.app
	@rm -f bin/databaseManager/*.app
	@rm -rf test/logs
	@rm -rf test/results
	@echo Repo cleaned

install:
