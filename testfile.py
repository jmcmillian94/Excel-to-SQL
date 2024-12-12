#import libraries
import pandas as pd
import sqlite3
import os

# define function needed to convert excel file to SQL table
def convertExcelToSQL(fileToConvert,dbName,tableName):
    # create pandas data frame from excel file
    df = pd.read_excel(fileToConvert)

    # create a connection to the SQLite database
    dbConnect = sqlite3.connect(dbName + '.db')

    # export dataframe to SQL table
    df.to_sql(tableName, dbConnect, if_exists='replace', index=False)

    # close database connection
    dbConnect.close()

    # print message confirming database was created/updated
    print(f"Database '{dbName}.db' created successfully")

# define function needed to convert csv file to SQL table
def convertCSVToSQL(fileToConvert,dbName,tableName):
    # create pandas data frame from excel file
    df = pd.read_csv(fileToConvert)

    # create a connection to the SQLite database
    dbConnect = sqlite3.connect(dbName + '.db')

    # export dataframe to SQL table
    df.to_sql(tableName, dbConnect, if_exists='replace', index=False)

    # close database connection
    dbConnect.close()

    # print message confirming database was created/updated
    print(f"Database '{dbName}.db' created successfully")

# main execution block
if __name__ == "__main__":
    while True:
        choice = input("Are you using an excel file(1) or a csv file(2)?")
        try:
            if choice == '1':
                fileToConvert = input("Enter the path of the Excel file (including .xlsx extension): ")
                # Validate if the file exists
                if not os.path.exists(fileToConvert):
                    print("Error: The specified Excel file does not exist. Please check the file path.")
                else:
                    dbName = input("Enter the name for the SQL database (without extension): ")
                    tableName = input("Enter the name for the SQL table:")
                    convertExcelToSQL(fileToConvert, dbName,tableName)
            if choice == '2':
                fileToConvert = input("Enter the path of the csv file (including .csv extension): ")
                # Validate if the file exists
                if not os.path.exists(fileToConvert):
                    print("Error: The specified CSV file does not exist. Please check the file path.")
                else:
                    dbName = input("Enter the name for the SQL database (without extension): ")
                    tableName = input("Enter the name for the SQL table:")
                    convertCSVToSQL(fileToConvert, dbName,tableName)
        except ValueError:
            print("invalid choice. Please select again")
            continue

    
    
