execution: bin/executeJob.app
	
bin/executeJob.app: src/executeJob.py pythonInterpreter
	@mkdir -p bin
	@cat pythonInterpreter src/executeJob.py > bin/executeJob.app
	@echo executeJob done