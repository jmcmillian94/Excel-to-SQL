# Excel-to-SQL
A simple tool that take an excel or csv file and converts it to a SQLite table.

First the program will ask for a database file path. If it finds one at the designated path it will allow you to modify it by adding or replacing tables. If it does not find a database it will create one.

Next, it will ask for a filepath to whichever Excel or CSV file you would like to use.

Once a file has been selected it will then promp you for a table name. Note that if a table name that already exists in the database you are using is used it will overwrite that table.

Once the table is created it will then list all columns in the newly created table and give you the option to designate one as a primary key. Note that multiple column names can be slected in order to create a composite key.

Once the table has been created it gives you the option to create additional tables or exit the program.

You may type 'quit' at any time in order to terminate the program.
