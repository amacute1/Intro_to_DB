import mysql.connector

# Database connection details
# IMPORTANT: Replace 'Sweetbabe1991?' with your actual root password
# You don't need to specify a database here initially, as we are creating one.
# Connect to the MySQL server itself.
mydb = None # Initialize mydb to None
mycursor = None # Initialize mycursor to None

try:
    # Establish connection to the MySQL server (without specifying a database)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sweetbabe1991?" # Your actual root password
    )

    # Check if the connection was successful
    if mydb.is_connected():
        print("Successfully connected to MySQL server!")

        # Get a cursor object
        mycursor = mydb.cursor()

        # SQL statement to create the database if it doesn't exist
        create_db_sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the SQL statement
        mycursor.execute(create_db_sql)

        print("Database 'alx_book_store' created successfully!")

    else:
        print("Failed to connect to MySQL server.")

except mysql.connector.Error as err:
    # Handle connection or execution errors
    print(f"Error: Failed to connect to the database or execute query: {err}")

finally:
    # Ensure the cursor and connection are closed
    if mycursor:
        mycursor.close()
        # print("Cursor closed.") # Optional: uncomment for more verbose output
    if mydb and mydb.is_connected():
        mydb.close()
        # print("Database connection closed.") # Optional: uncomment for more verbose output
    else:
        print("No connection was established to close.")
