#import libraries
import pandas as pd
import sqlite3
import os

# Function to convert Excel to SQL
def convert_to_sql(excel_file, db_name):
    # Read Excel file into pandas DataFrame
    df = pd.read_excel(excel_file)
    
    # Create SQLite connection
    conn = sqlite3.connect(db_name + ".db")
    
    # Export DataFrame to SQL table
    df.to_sql("table_name", conn, if_exists='replace', index=False)
    
    # Close the connection
    conn.close()
    
    # Confirm to the user that the database was created
    print(f"Database '{db_name}.db' created successfully in the current directory!")

# Main execution block
if __name__ == "__main__":
    # Ask for the Excel file path and database name
    excel_file = input("Enter the path of the Excel file (including .xlsx extension): ")
    
    # Validate if the file exists
    if not os.path.exists(excel_file):
        print("Error: The specified Excel file does not exist. Please check the file path.")
    else:
        db_name = input("Enter the name for the SQL database (without extension): ")
        convert_to_sql(excel_file, db_name)