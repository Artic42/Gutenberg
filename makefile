include makefiles/databaseManager.make


all: databaseManager

clean: 
	@rm -rf bin
	@echo Repo cleaned

install: 