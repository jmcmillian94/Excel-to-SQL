#import libraries
import pandas as pd
import sqlite3
import os
import time

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
    print('SQLite Database Creation Tool')
    print("\nThis program will take any Excel or CSV file and convert it to a table for the specified SQLite database.")
    time.sleep(3)
    while True:
        choice = input("\nPlease select the file type you are using by typing the corresponding number or type 'q' to quit the program\n \n 1.) Excel\n 2.) CSV\n\n=>")
        try:
            if choice == '1':
                fileToConvert = input("Enter the path of the Excel file (including .xlsx extension): ")
                # Validate if the file exists
                if not os.path.exists(fileToConvert):
                    print("Error: The specified Excel file does not exist. Please check the file path. Returning to start...")
                else:
                    dbName = input("Enter the name for the SQLite database (without extension) to be created or modified: ")
                    tableName = input("Enter the name for the SQL table. An existing table with the same name will be overwritten in the database:")
                    convertExcelToSQL(fileToConvert, dbName,tableName)
            if choice == '2':
                fileToConvert = input("Enter the path of the csv file (including .csv extension): ")
                # Validate if the file exists
                if not os.path.exists(fileToConvert):
                    print("Error: The specified CSV file does not exist. Please check the file path.")
                else:
                    dbName = input("Enter the name for the SQLite database (without extension) to be created or modified: ")
                    tableName = input("Enter the name for the SQL table. An existing table with the same name will be overwritten in the database:")
                    convertCSVToSQL(fileToConvert, dbName,tableName)
            if choice == 'q':
                exit()
        except ValueError:
            print("An error occured. Returning to start...")
            continue

    
    
