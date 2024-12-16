##############################
###### import libraries ######
##############################
import pandas as pd
import sqlite3
import time
import os
import sys

##############################
###### define functions ######
##############################

# function that takes a file and converts it to a SQL table 
def convertFileToSQLiteTable(fileToConvert,dbName,tableName):
    if fileToConvert.lower().endswith(('.xlsx', '.xls')):
        df = pd.read_excel(fileToConvert)
        
    else:
        df = pd.read_csv(fileToConvert)
    
    dbConnect = sqlite3.connect(dbName)
    df.to_sql(tableName, dbConnect, if_exists='replace', index=False)
    dbConnect.close()
    print(f"Table added to'{dbName}' successfully")

# this function terminates the program at anytime if the user types quit
def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'quit':
        print("Exiting program...")
        time.sleep(1)
        sys.exit()  # Terminate the program
    return user_input


#############################
###### main code block ######
#############################

#print intro text
print("Welcome to the SQL Database Creation Tool\n")

print("This program will take any Excel or CSV file and convert it to a table for the specified SQLite database.\n")

print("Type 'quit' at anytime to terminate the program.\n")

dbName = get_input("Please enter the filepath and name for the database you would like to use (either a new db or an existing one):\n")

if os.path.exists(dbName) == True:
    print("Database found. You may now update it.\n")
else:
    print("No Database with that path exists. A new database will be created.\n")

while True: #start an infinite loop for adding multiple tables
    while True:
        fileToConvert = get_input("Please enter the filepath for the excel or csv file you would like to convert to a table:\n")
        if os.path.exists(fileToConvert):
            break
        else:
            print('invalid file path. please try again.')

        
    tableName = get_input("Please enter a name for the table (existing tables of the same name will be overwritten!):\n")
    convertFileToSQLiteTable(fileToConvert,dbName,tableName)
        
    menuChoice = get_input("Would you like to add another table to the database? y/n\n")
    if menuChoice != 'y':
        print("Closing program...")
        time.sleep(1)
        break

