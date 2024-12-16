##############################
###### import libraries ######
##############################
import pandas as pd
import sqlite3
import time
import os

##############################
###### define functions ######
##############################

# function that takes a file and converts it to a SQL table 
# *right now only works with excel file, need to add csv functionality
def convertFileToSQLiteTable(fileToConvert,dbName,tableName):
    df = pd.read_excel(fileToConvert)
    dbConnect = sqlite3.connect(dbName)
    df.to_sql(tableName, dbConnect, if_exists='replace', index=False)
    dbConnect.close()
    print(f"Table added to'{dbName}' successfully")


#############################
###### main code block ######
#############################

#print intro text
print("SQL Database Creation Tool")

print("This program will take any Excel or CSV file and convert it to a table for the specified SQLite database.")

dbName = input("Please enter the filepath and name for the database you would like to use (either a new db or an existing one):")

while True: #start an infinite loop for adding multiple tables
    while True:
        fileToConvert = input("Please enter the filepath for the excel or csv file you would like to convert to a table:")
        if os.path.exists(fileToConvert):
            break
        else:
            print('invalid file path. please try again.')

        
    tableName = input("Please enter a name for the table (existing tables of the same name will be overwritten!):")
    convertFileToSQLiteTable(fileToConvert,dbName,tableName)
        
    menuChoice = input("Would you like to add another table to the database? y/n\n")
    if menuChoice != 'y':
        print("Closing program...")
        time.sleep(2)
        break

#ask what the user would like to do and wait for input
#menuChoice = input("Would you like to create a new database? Or add to an Existing one?\n1.) Create new\n2.) Update Existing\n3.) Exit Program\n")


#determine what happens based on menu choice
#if menuChoice == '1':
#    dbName = input("Please enter the filepath and name of the new database:")
#
#    while True: #start an infinite loop for adding multiple tables
#        fileToConvert = input("Please enter the filepath for the excel or csv file you would like to convert to a table:")
#        tableName = input("Please enter a name for the table:")
#        convertFileToSQLiteTable(fileToConvert,dbName,tableName)
#        
#        menuChoice2 = input("Would you like to add another table to the database? y/n\n")
#        if menuChoice2 != 'y':
#            print("Closing program...")
#            time.sleep(2)
#            break
#
#if menuChoice == '2':
#    dbName = input("Please enter the filepath and name for the new database")
#
#
#else:
#    print("Closing program...")
#    time.sleep(2)
#    break
    
