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
    return df.columns  # Return the column names for further processing

# function to recreate table with a primary key
def recreateTableWithPrimaryKey(dbName, tableName, columns, primaryKeys):
    dbConnect = sqlite3.connect(dbName)
    cursor = dbConnect.cursor()

    try:
        # Retrieve the data from the existing table
        cursor.execute(f"SELECT * FROM {tableName}")
        rows = cursor.fetchall()

        # Convert columns to a list to avoid Index errors
        columns = list(columns)

        # Drop the existing table
        cursor.execute(f"DROP TABLE IF EXISTS {tableName}")

        # Create a new table schema with the composite primary key
        columns_with_types = [f'"{col}" TEXT' for col in columns]  # Assuming TEXT as default type
        if primaryKeys:
            primary_key_clause = f", PRIMARY KEY ({', '.join([f'\"{pk}\"' for pk in primaryKeys])})"
        else:
            primary_key_clause = ""
        create_table_query = f"CREATE TABLE \"{tableName}\" ({', '.join(columns_with_types)}{primary_key_clause})"
        cursor.execute(create_table_query)

        # Insert the data back into the new table
        placeholders = ', '.join(['?' for _ in columns])
        cursor.executemany(f"INSERT INTO \"{tableName}\" VALUES ({placeholders})", rows)

        dbConnect.commit()
        print(f"Primary key(s) {', '.join(primaryKeys)} added to table '{tableName}' successfully")

    except sqlite3.IntegrityError as e:
        # Handle unique constraint failure
        print(f"Error: Cannot set column(s) {', '.join(primaryKeys)} as primary key(s). {str(e)}")
        print("Rolling back changes...")
        dbConnect.rollback()  # Revert to the previous state

        # Ensure the partially created table is removed
        cursor.execute(f"DROP TABLE IF EXISTS {tableName}")

        # Recreate the original table without primary key changes
        columns_with_types = [f'"{col}" TEXT' for col in columns]
        create_table_query = f"CREATE TABLE \"{tableName}\" ({', '.join(columns_with_types)})"
        cursor.execute(create_table_query)

        # Reinsert the original data
        cursor.executemany(f"INSERT INTO \"{tableName}\" VALUES ({placeholders})", rows)
        dbConnect.commit()

        print("Table restored without primary key changes.")

    finally:
        dbConnect.close()





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

if os.path.exists(dbName):
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
    columns = convertFileToSQLiteTable(fileToConvert,dbName,tableName)

    # Ask if the user wants to add primary keys
    print("\nThe following columns are available in the table:")
    for idx, column in enumerate(columns, 1):
        print(f"{idx}. {column}")
    
    primaryKeys = []
    while True:
        pkChoice = get_input("Enter the column name to set as a primary key (or type 'done' if finished):\n")
        if pkChoice.lower() == 'done':
            break
        elif pkChoice in columns:
            primaryKeys.append(pkChoice)
            print(f"Column '{pkChoice}' added as a primary key.")
        else:
            print("Invalid column name. Please try again.")

    if primaryKeys:
        recreateTableWithPrimaryKey(dbName, tableName, columns, primaryKeys)
        
    menuChoice = get_input("Would you like to add another table to the database? y/n\n")
    if menuChoice != 'y':
        print("Closing program...")
        time.sleep(1)
        break


