import pandas as pd
import sqlite3
import time
import os

def convertFileToSQLiteTable(fileToConvert,dbName,tableName):
    df = pd.read_excel(fileToConvert)
    dbConnect = sqlite3.connect(dbName)
    df.to_sql(tableName, dbConnect, if_exists='replace', index=False)
    dbConnect.close()
    print(f"Table added to'{dbName}' successfully")

print("SQL Database Creation Tool")

print("This program will take any Excel or CSV file and convert it to a table for the specified SQLite database.")

menuChoice = input("Would you like to create a new database? Or add to an Existing one?\n1.) Create new\n2.) Update Existing\n3.) Exit Program\n")

if menuChoice == '1':
    dbName = input("Please enter the filepath and name of the new database:")

    while True: #start an infinite loop for adding multiple tables
        fileToConvert = input("Please enter the filepath for the excel or csv file you would like to convert to a table:")
        tableName = input("Please enter a name for the table:")
        convertFileToSQLiteTable(fileToConvert,dbName,tableName)
        
        menuChoice2 = input("Would you like to add another table to the database? y/n\n")
        if menuChoice2 != 'y':
            print("Closing program...")
            time.sleep(2)
            break

else:
    print("Closing program...")
    time.sleep(2)
    exit()
    
