# Database manager test suite

This is a test sutie desing to test the functionality of the database manager in the Gutenberg project. The are diferent modules that will be tested separatedly. The epyc have been separated on the following modules.

- Creation of database
- Insertion and deletion of all element types
- Export entire database
- Import entire database
- Export entry of template, color, color pallete and generator
- Import entry of template, color, color pallete and generator

One python script will run the entire set of test and compare it with reference documents in the porject folder. Test references.

## Creation of database

The create database script will be runned. The result should be equal to the database *test/databaseManager/referenceFiles/emptyDatabase.db* The test will run on script *test/databaseManager/createDatabaeTest.py*.

## Insertion and deletion of all element types

The test will run the following action with each element

- Insert item 1
- Insert item 1 again and check fail status is present
- Insert item 2
- Insert item 3
- Delete item 1

When this test have been runned with all the types the database will be compared with  *test/databaseManager/fullDatabase.db*

The test will be programmed in *test/databaseManager/insertDeleteTest.py*

## Export entire database

The test will export the database on *test/databaseManager/fullDatabase.db* into a json file and compare it with *test/databaseManager/fullDatabase.json*

The test will be programmed in *test/databaseManager/exportDatabaseTest.py*

## Import entire database

The test will import the file *test/databaeManager/fullDatabase.json*. Check that the result database is the same as *test/databaseManager/fullDatabase.db*

The test will be programmed in *test/databaseManager/importDatabaseTest.py*